"""CEP v2.1.1 - Minimal validator sketches

NOTE:
- This file is intentionally small and opinionated.
- Expand per your per-pass schemas and integration stack.
"""

import re
from typing import Any, Iterator, Tuple

EVIDENCE_RE = re.compile(r"\[EVIDENCE:\s*p\.\d+(?:-\d+)?(?:,\s*p\.\d+(?:-\d+)?)*\]")

def walk_strings(obj: Any, path: str = "") -> Iterator[Tuple[str, str]]:
    """Yield (json_pointer, value) for all string leaves in a nested dict/list."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, path + "/" + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, path + "/" + str(i))
    elif isinstance(obj, str):
        yield (path or "/", obj)

def has_evidence(text: str) -> bool:
    if text.strip() == "Not defined in source":
        return True
    return bool(EVIDENCE_RE.search(text))

def validate_evidence(obj: Any) -> list[str]:
    """Return list of errors for missing evidence tags."""
    errors: list[str] = []
    for json_ptr, value in walk_strings(obj):
        # Example exemption convention:
        if json_ptr.endswith("/verbatim_canon"):
            continue
        if not has_evidence(value):
            errors.append(f"Missing evidence at {json_ptr}")
    return errors

def validate_verbatim_blocks(blocks: list[dict], page_text_raw_by_page: dict[int, str]) -> list[str]:
    """Validate that each excerpt exists as a substring in PageText_Raw over the cited page range."""
    errors: list[str] = []
    for b in blocks:
        pages = range(int(b["page_start"]), int(b["page_end"]) + 1)
        haystack = "\n".join(page_text_raw_by_page[p] for p in pages)
        if b["excerpt_raw"] not in haystack:
            errors.append(f"P2 excerpt not found (block_id={b.get('block_id')})")
    return errors

def validate_canon_write(write_request: dict) -> None:
    """Block canonical writes that are not decision-gated."""
    table = write_request.get("table_name", "")
    if table.endswith("_Canon") and write_request.get("operation") in {"update", "upsert"}:
        if not write_request.get("decision_id"):
            raise ValueError("Canon write blocked: missing decision_id (X2).")

# --- CEP v2.1.1 expansion patch (P0/P1) ---
# Single source of truth for evidence tags:
EVIDENCE_RE = r"\[EVIDENCE:\s*p\.\d+(?:-\d+)?(?:,\s*p\.\d+(?:-\d+)?)*\]"

def validate_against_schema(data: dict, schema: dict) -> None:
    """
    Validate `data` against a JSON Schema dict. Raises an Exception on failure.
    NOTE: requires `jsonschema` in runtime environment.
    """
    import jsonschema
    jsonschema.validate(instance=data, schema=schema)

def validate_register(value: str) -> None:
    allowed = {"Canon", "Operator", "Combustion", "Unclear"}
    if value not in allowed:
        raise ValueError(f"Invalid register: {value}. Expected one of {sorted(allowed)}")

def validate_term_hash(term_surface: str, term_hash_sha256: str) -> None:
    import hashlib
    h = hashlib.sha256(term_surface.encode("utf-8")).hexdigest()
    if h != term_hash_sha256:
        raise ValueError(f"Term hash mismatch for term={term_surface!r}. Expected {h}, got {term_hash_sha256}")

def validate_gate_status(x1_manifest: dict, required: list[str]) -> None:
    gates = (x1_manifest or {}).get("gates", {})
    for gate_id in required:
        st = (gates.get(gate_id) or {}).get("status")
        if st != "PASS":
            raise ValueError(f"Gate {gate_id} status is {st!r}, expected 'PASS'")
# --- end patch ---

