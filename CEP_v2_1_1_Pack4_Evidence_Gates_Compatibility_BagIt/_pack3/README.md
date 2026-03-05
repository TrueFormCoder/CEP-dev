CEP v2.1.1 — Pack #3: Tooling + Tests + Fixtures Generator

Includes
- pre-commit: ruff + formatting + schema checks
- pyproject.toml: ruff + pytest config
- requirements-dev.txt: jsonschema + pytest
- scripts/generate_fixtures.py: deterministic fixtures generator
- tests/: validator unit tests + fixture generator smoke test
- CI workflow: python 3.10/3.11/3.12 matrix

How to use
1) Copy into repo root (merge directories)
2) Run:
   pip install -r requirements-dev.txt
   pre-commit install
   pytest
3) CI will run automatically on PRs/pushes.

Generated: 2026-03-05T12:51:06.087755+00:00
