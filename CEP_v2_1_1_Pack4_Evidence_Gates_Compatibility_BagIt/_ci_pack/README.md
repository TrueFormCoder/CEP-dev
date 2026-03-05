CEP v2.1.1 — CI + Fixtures + Policies Pack

Purpose
- Makes the repo self-enforcing:
  - JSON Schemas load correctly
  - Minimal fixtures validate (P0–P3 + checkpoint)
  - Governance policies are explicit and versioned

Includes
- .github/workflows/cep-validate.yml
- scripts/validate_schemas_load.py
- scripts/validate_fixtures.py
- fixtures/v2.1.1/*.json
- policies/*.md
- schemas/*.schema.json (copied from the generated schema pack)

Generated: 2026-03-05T12:44:01.396535+00:00
