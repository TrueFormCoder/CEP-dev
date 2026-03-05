"""
Minimal BagIt verification (SHA-256 manifest) scaffolding.

This is intentionally simple so it can run in CI without extra deps.
Assumes:
- tag file: bagit.txt exists
- payload manifest: manifest-sha256.txt exists at bag root
- payload files in ./data/
"""
import hashlib
from pathlib import Path

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def parse_manifest(manifest_path: Path):
    # BagIt format: "<hash>  <relative_path>"
    entries = {}
    for line in manifest_path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            raise ValueError(f"Bad manifest line: {line!r}")
        digest = parts[0]
        rel = " ".join(parts[1:]).strip()
        entries[rel] = digest
    return entries

def verify_bag(bag_root: Path) -> None:
    if not (bag_root/"bagit.txt").exists():
        raise FileNotFoundError("bagit.txt missing")
    manifest = bag_root/"manifest-sha256.txt"
    if not manifest.exists():
        raise FileNotFoundError("manifest-sha256.txt missing")
    entries = parse_manifest(manifest)
    # Verify every entry
    for rel, expected in entries.items():
        fp = bag_root/rel
        if not fp.exists():
            raise FileNotFoundError(f"Payload missing: {rel}")
        got = sha256_file(fp)
        if got != expected:
            raise ValueError(f"SHA256 mismatch for {rel}: expected {expected}, got {got}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--bag", required=True, help="Path to BagIt root")
    args = ap.parse_args()
    verify_bag(Path(args.bag))
    print("OK: bag verified")
