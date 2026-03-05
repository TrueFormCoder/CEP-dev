"""
Schema compatibility checker.

Used by Delta Mode (X3) and CI to avoid comparing incompatible artifacts.
"""
import json
from pathlib import Path

def load_map() -> dict:
    return json.loads(Path("schemas/compatibility_map.json").read_text())

def is_compatible(a: str, b: str) -> bool:
    m = load_map()
    compat = m.get("compatible_with", {})
    return (b in compat.get(a, [])) or (a in compat.get(b, []))

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    args = ap.parse_args()
    ok = is_compatible(args.a, args.b)
    print("COMPATIBLE" if ok else "INCOMPATIBLE")
    raise SystemExit(0 if ok else 2)
