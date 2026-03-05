import re
import json
from pathlib import Path

from validators.validators_minimal import EVIDENCE_RE
from scripts.evidence_coverage import compute_evidence_coverage_pct, enforce_threshold

def test_evidence_coverage_pct():
    obj = {"a":"[EVIDENCE: p.1]", "b":"Not defined in source", "c":"missing"}
    pct, covered, total = compute_evidence_coverage_pct(obj, EVIDENCE_RE)
    assert total == 3
    assert covered == 2
    assert abs(pct - (2/3)) < 1e-9

def test_evidence_thresholds():
    obj = {"a":"[EVIDENCE: p.1]", "b":"Not defined in source", "c":"missing"}
    assert enforce_threshold(obj, EVIDENCE_RE, warn_threshold=0.90) == "BLOCK"
    obj2 = {"a":"[EVIDENCE: p.1]", "b":"Not defined in source", "c":"[EVIDENCE: p.2]"}
    assert enforce_threshold(obj2, EVIDENCE_RE, warn_threshold=0.90) == "PASS"
