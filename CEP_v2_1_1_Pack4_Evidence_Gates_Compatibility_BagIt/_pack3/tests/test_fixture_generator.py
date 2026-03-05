from pathlib import Path
import subprocess
import sys

def test_fixture_generator_runs(tmp_path: Path):
    out = tmp_path / "fixtures"
    cmd = [sys.executable, "scripts/generate_fixtures.py", "--out", str(out), "--run-id",
           "123e4567-e89b-72d3-a456-426614174000", "--source-id", "SRC01"]
    subprocess.check_call(cmd)
    for name in ["p0_source_index.json","p1_construct_inventory.json","p1q_qa_instrumentation.json",
                 "p2_verbatim_blocks.json","p3_definitions.json","checkpoint.json"]:
        assert (out/name).exists()
