Gate Canonical Source Policy (v2.1.1)

Rule
- X1 manifest is canonical for gate status (G1/G2/G3).
- Any derived gate report (markdown, PDF, Slack message) must be a view of X1 and MUST NOT contradict it.

Enforcement
- If a gate report contradicts X1: BLOCK archival and reviewer sign-off.
- Validator: scripts/gate_consistency.py validate_gate_report_matches_x1()
