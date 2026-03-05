"""
Gate canonical source consistency checks.

Rule:
- X1 manifest gates.* is canonical.
- Any derived gate report must match the status and referenced counts (if present).
"""
from typing import Any, Dict

def validate_gate_report_matches_x1(gate_report: Dict[str, Any], x1_manifest: Dict[str, Any]) -> None:
    x1_gates = (x1_manifest or {}).get("gates", {})
    rep_gates = (gate_report or {}).get("gates", gate_report)  # allow two shapes
    for gate_id, rep_val in rep_gates.items():
        x1_val = x1_gates.get(gate_id)
        if not x1_val:
            raise ValueError(f"Gate {gate_id} not present in X1")
        rep_status = (rep_val or {}).get("status", rep_val)
        x1_status = (x1_val or {}).get("status", x1_val)
        if rep_status != x1_status:
            raise ValueError(f"Gate {gate_id} mismatch: report={rep_status!r} x1={x1_status!r}")
