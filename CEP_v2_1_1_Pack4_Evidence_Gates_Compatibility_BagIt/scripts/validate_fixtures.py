import json
from pathlib import Path
import jsonschema

def load_schema(name: str) -> dict:
    return json.loads(Path("schemas")/name).read_text()

schemas = {}
schemas_dir = Path("schemas")
for p in schemas_dir.glob("*.schema.json"):
    schemas[p.name] = json.loads(p.read_text())

mapping = {
    "p0_source_index.json": "p0-source-index.schema.json",
    "p1_construct_inventory.json": "p1-construct-inventory.schema.json",
    "p1q_qa_instrumentation.json": "p1q-qa-instrumentation.schema.json",
    "p2_verbatim_blocks.json": "p2-verbatim-blocks.schema.json",
    "p3_definitions.json": "p3-definitions.schema.json",
    "checkpoint.json": "checkpoint.schema.json",
}

fixtures_dir = Path("fixtures/v2.1.1")
fx_files = sorted(fixtures_dir.glob("*.json"))
if not fx_files:
    raise SystemExit("No fixtures found in fixtures/v2.1.1")

for fx in fx_files:
    schema_name = mapping.get(fx.name)
    if not schema_name:
        raise SystemExit(f"No schema mapping for fixture {fx.name}")
    schema = schemas[schema_name]
    data = json.loads(fx.read_text())
    jsonschema.validate(instance=data, schema=schema)

print(f"OK: validated {len(fx_files)} fixtures")
