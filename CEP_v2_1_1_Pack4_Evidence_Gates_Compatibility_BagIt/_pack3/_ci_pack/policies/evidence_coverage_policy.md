CEP Evidence Coverage Policy (v2.1.1)

Purpose
- Prevent ambiguous enforcement when some fields are tagged and others are not.

Policy
- Compute evidence_coverage_pct = (# string fields that meet evidence requirement) / (# string fields that require evidence)
- A field meets the requirement if:
  - it contains at least one valid evidence tag: [EVIDENCE: p.X] (or range/list), OR
  - it equals exactly: Not defined in source

Enforcement
- coverage_pct >= 0.90: WARN + archive allowed; create Linear “EvidenceRepairQueue” issue for missing fields.
- coverage_pct < 0.90: BLOCK + do not archive; create Linear issue; rerun pass after repairs.

Canonical Source of Truth
- validators_minimal.py::EVIDENCE_RE is authoritative for the evidence tag pattern.
