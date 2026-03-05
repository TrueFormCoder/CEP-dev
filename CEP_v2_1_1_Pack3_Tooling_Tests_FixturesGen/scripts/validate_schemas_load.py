import json
from pathlib import Path

schemas_dir = Path("schemas")
schema_files = sorted([p for p in schemas_dir.glob("*.json") if p.is_file()])
if not schema_files:
    raise SystemExit("No schema files found in ./schemas")
for p in schema_files:
    json.loads(p.read_text())
print(f"OK: loaded {len(schema_files)} schema files")
