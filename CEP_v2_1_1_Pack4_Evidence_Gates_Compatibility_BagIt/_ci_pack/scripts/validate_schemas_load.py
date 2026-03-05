import json
from pathlib import Path

schemas_dir = Path("schemas")
schema_files = sorted([p for p in schemas_dir.glob("*.json") if p.is_file()])

if not schema_files:
    raise SystemExit("No schemas found in ./schemas")

for p in schema_files:
    try:
        json.loads(p.read_text())
    except Exception as e:
        raise SystemExit(f"Schema JSON invalid: {p}: {e}")

print(f"OK: loaded {len(schema_files)} schema JSON files")
