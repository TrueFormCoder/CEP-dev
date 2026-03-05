Pack #4 — Evidence + Gates + Compatibility + BagIt (v2.1.1)

Adds:
- scripts/evidence_coverage.py + tests
- scripts/gate_consistency.py + tests
- schemas/compatibility_map.json + scripts/check_schema_compatibility.py + tests
- scripts/verify_bagit.py scaffolding
- policies for evidence coverage + gate canonical source + BagIt tooling pin

CI:
- runs schema compatibility self-check in the matrix build

Generated: 2026-03-05T13:07:32.172910+00:00
