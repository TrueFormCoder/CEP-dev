import json
from pathlib import Path
import jsonschema

schemas = {}
schemas_dir = Path("schemas")
for p in schemas_dir.glob("*.schema.json"):
    schemas[p.name] = json.loads(p.read_text())

def get_schema_for_fixture(fname: str):
    mapping = {
        "p0_source_index.json": "p0-source-index.schema.json",
        "p1_construct_inventory.json": "p1-construct-inventory.schema.json",
        "p1q_qa_instrumentation.json": "p1q-qa-instrumentation.schema.json",
        "p2_verbatim_blocks.json": "p2-verbatim-blocks.schema.json",
        "p3_definitions.json": "p3-definitions.schema.json",
        "checkpoint.json": "checkpoint.schema.json",
    }
    key = mapping.get(fname)
    if not key:
        raise KeyError(f"No schema mapping for fixture {fname}")
    return schemas[key]

fixtures_dir = Path("fixtures/v2.1.1")
fx_files = sorted([p for p in fixtures_dir.glob("*.json") if p.is_file()])
if not fx_files:
    raise SystemExit("No fixtures found")

ok = 0
for fx in fx_files:
    data = json.loads(fx.read_text())
    schema = get_schema_for_fixture(fx.name)
    jsonschema.validate(instance=data, schema=schema)
    ok += 1

print(f"OK: validated {ok} fixtures")
