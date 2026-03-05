"""
Generate deterministic CEP fixture artifacts for CI from a single seed.

Usage:
  python scripts/generate_fixtures.py --out fixtures/v2.1.1 --run-id <uuidv7> --source-id SRC01

Notes:
- This generator does NOT claim to produce semantically correct CEP artifacts.
- It produces schema-valid "golden samples" to prevent schema drift.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="Output directory, e.g. fixtures/v2.1.1")
    ap.add_argument("--run-id", required=True, help="UUIDv7 string (best-effort)")
    ap.add_argument("--source-id", default="SRC01")
    args = ap.parse_args()

    out = Path(args.out)
    run_id = args.run_id
    source_id = args.source_id

    term = "CEP"
    excerpt = "CEP is a deterministic archival compiler."

    p0 = {
      "schema_version": "v2.1.1",
      "run_id": run_id,
      "created_at": now_iso(),
      "sources": [{
        "source_id": source_id,
        "filename": "example-thread.pdf",
        "sha256": "a"*64,
        "bytes": 123456,
        "page_count": 10,
        "vault_uri": f"vault://cep/2026/{run_id}/sources/example-thread.pdf",
        "drive_uri": f"drive://CEP/Runs/2026/{run_id}/example-thread.pdf",
        "ingested_at": now_iso(),
        "notes": "Fixture source for CI validation"
      }]
    }

    p1 = {
      "schema_version": "v2.1.1",
      "run_id": run_id,
      "source_id": source_id,
      "created_at": now_iso(),
      "constructs": [{
        "construct_id": "CNSTR001",
        "term": term,
        "term_hash_sha256": sha256_hex(term),
        "type": "System",
        "first_seen": "p.1",
        "footprint_pages": ["p.1","p.2"],
        "aliases": ["Codex Extraction Protocol"],
        "register": "Operator",
        "notes": "Fixture construct"
      }]
    }

    p1q = {
      "schema_version": "v2.1.1",
      "run_id": run_id,
      "source_id": source_id,
      "created_at": now_iso(),
      "qa_items": [{
        "construct_id": "CNSTR001",
        "noise_flag": False,
        "priority_score": 92.0,
        "priority_band": "A",
        "suggested_type": "System",
        "suggested_register": "Operator",
        "suggested_alias_cluster": ["CEP","Codex Extraction Protocol"],
        "footprint_recalc_pages": ["p.1","p.2","p.3"],
        "downstream_eligible": True,
        "rationale": "High centrality term; likely referenced in multiple passes."
      }]
    }

    p2 = {
      "schema_version": "v2.1.1",
      "run_id": run_id,
      "source_id": source_id,
      "created_at": now_iso(),
      "blocks": [{
        "block_id": "BLK0001",
        "construct_id": "CNSTR001",
        "page_start": 1,
        "page_end": 1,
        "excerpt_raw": excerpt,
        "excerpt_sha256": sha256_hex(excerpt),
        "capture_method": "manual_extract",
        "notes": "Fixture excerpt"
      }]
    }

    p3 = {
      "schema_version": "v2.1.1",
      "run_id": run_id,
      "source_id": source_id,
      "created_at": now_iso(),
      "definitions": [{
        "construct_id": "CNSTR001",
        "term": term,
        "register": "Operator",
        "verbatim_canon": {"text": "CEP", "evidence": "Not defined in source"},
        "interpretation": {"text": "A deterministic archival compiler pipeline.", "evidence": "[EVIDENCE: p.1]"},
        "fields": {
          "purpose": "[EVIDENCE: p.1]",
          "nonnegotiables": "Not defined in source"
        }
      }]
    }

    checkpoint = {
      "schema_version": "v2.1.1",
      "run_id": run_id,
      "last_completed_pass": "P2",
      "session_id": "session_fixture_001",
      "timestamp": now_iso(),
      "artifacts": [
        {"name":"p0", "uri":"drive://...", "sha256":"b"*64, "pass":"P0", "schema_id": "urn:cep:schema:p0-source-index:v2.1.1"},
        {"name":"p1", "uri":"drive://...", "sha256":"c"*64, "pass":"P1", "schema_id": "urn:cep:schema:p1-construct-inventory:v2.1.1"},
      ]
    }

    write_json(out/"p0_source_index.json", p0)
    write_json(out/"p1_construct_inventory.json", p1)
    write_json(out/"p1q_qa_instrumentation.json", p1q)
    write_json(out/"p2_verbatim_blocks.json", p2)
    write_json(out/"p3_definitions.json", p3)
    write_json(out/"checkpoint.json", checkpoint)

    print(f"Generated fixtures in {out}")

if __name__ == "__main__":
    main()
