import re
import pytest
import hashlib

from validators.validators_minimal import (
    EVIDENCE_RE,
    validate_register,
    validate_term_hash,
)

def test_evidence_regex_matches():
    assert re.search(EVIDENCE_RE, "[EVIDENCE: p.1]")
    assert re.search(EVIDENCE_RE, "[EVIDENCE: p.12-14]")
    assert re.search(EVIDENCE_RE, "[EVIDENCE: p.1, p.2, p.10-12]")

def test_validate_register_ok():
    for v in ["Canon","Operator","Combustion","Unclear"]:
        validate_register(v)

def test_validate_register_bad():
    with pytest.raises(ValueError):
        validate_register("canon")  # wrong case

def test_validate_term_hash_ok_and_bad():
    term = "CEP"
    h = hashlib.sha256(term.encode("utf-8")).hexdigest()
    validate_term_hash(term, h)
    with pytest.raises(ValueError):
        validate_term_hash(term, "0"*64)
