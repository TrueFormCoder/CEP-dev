from scripts.gate_consistency import validate_gate_report_matches_x1
import pytest

def test_gate_report_matches():
    x1 = {"gates":{"G1":{"status":"PASS"},"G3":{"status":"PASS"}}}
    report = {"gates":{"G1":{"status":"PASS"},"G3":{"status":"PASS"}}}
    validate_gate_report_matches_x1(report, x1)

def test_gate_report_mismatch_blocks():
    x1 = {"gates":{"G1":{"status":"PASS"}}}
    report = {"gates":{"G1":{"status":"FAIL"}}}
    with pytest.raises(ValueError):
        validate_gate_report_matches_x1(report, x1)
