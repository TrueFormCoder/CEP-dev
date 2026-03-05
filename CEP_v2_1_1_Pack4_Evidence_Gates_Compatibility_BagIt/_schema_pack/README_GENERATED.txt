CEP v2.1.1 — P0→P3 Schema Pack (Generated)

Contents:
- /schemas/*.schema.json
  - defs.schema.json (shared defs)
  - p0-source-index.schema.json
  - p1-construct-inventory.schema.json
  - p1q-qa-instrumentation.schema.json
  - p2-verbatim-blocks.schema.json
  - p3-definitions.schema.json
  - checkpoint.schema.json

Patches (non-breaking, proposed):
- x1-run-manifest.schema.patched.json
  Adds: pipeline pinning + checkpoint metadata + template_version field support.
- x2-decision-log-entry.schema.patched.json
  Adds: RUN_SIGNOFF enum value.
- validators_minimal.patched.py
  Adds: validate_against_schema(), validate_register(), validate_term_hash(), validate_gate_status()
  Sets EVIDENCE_RE as single source-of-truth.

Generated at: 2026-03-05T12:40:37.667728

Next: Apply these as diffs under the change control policy (MIRRORSOLVE v6).
