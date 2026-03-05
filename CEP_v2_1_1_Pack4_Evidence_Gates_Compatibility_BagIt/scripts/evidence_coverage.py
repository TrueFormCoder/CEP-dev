"""
Evidence coverage computation.

Policy:
- A string field is "covered" if:
  - it matches EVIDENCE_RE at least once, OR
  - it equals exactly "Not defined in source"
- Coverage is computed over all string leaves in the object.
"""
import re
from typing import Any, Tuple

NOT_DEFINED = "Not defined in source"

def walk_strings(obj: Any):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v)
    elif isinstance(obj, list):
        for it in obj:
            yield from walk_strings(it)
    elif isinstance(obj, str):
        yield obj

def compute_evidence_coverage_pct(obj: Any, evidence_re: str) -> Tuple[float, int, int]:
    rx = re.compile(evidence_re)
    total = 0
    covered = 0
    for s in walk_strings(obj):
        total += 1
        if s == NOT_DEFINED or rx.search(s):
            covered += 1
    pct = (covered / total) if total else 1.0
    return pct, covered, total

def enforce_threshold(obj: Any, evidence_re: str, warn_threshold: float = 0.90) -> str:
    pct, covered, total = compute_evidence_coverage_pct(obj, evidence_re)
    if pct >= warn_threshold:
        return "WARN" if pct < 1.0 else "PASS"
    return "BLOCK"
