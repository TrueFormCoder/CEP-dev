Write Queue Fallback Reconciliation (v2.1.1)

Problem
- Connector rate limits can force the pipeline to spill writes into batch files (JSON/CSV) in Drive.
- Without reconciliation, Airtable/Linear may be partially updated and drift from canonical artifacts.

Required Steps (Operator)
1) Every batch file name includes run_id + destination + monotonic batch index.
2) Every record includes an idempotency_key = sha256(run_id + destination + primary_key + payload_sha256).
3) After connector recovery, run reconciliation:
   - For each batch file, attempt write.
   - On success, write a reconciliation receipt with counts + failed keys.
   - Only then mark batch file “reconciled=true”.

Block Conditions
- Any unreconciled batch files for Canon writes => BLOCK sign-off.
- QA writes may WARN but must be reconciled within 24h.
