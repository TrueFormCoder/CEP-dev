BagIt Tooling Pin (v2.1.1)

Pinned tooling (recommended)
- bagit-python==1.8.1 (or pinned in lockfile)
- hashlib SHA-256 (stdlib)

Verification contract
1) Validate bag structure exists: bagit.txt, manifest-*.txt, data/
2) Every payload file appears exactly once in manifest-sha256.txt
3) Recompute sha256 for each payload file and compare to manifest
4) Fail if any mismatch
