OCR Triage Threshold (v2.1.1)

Goal
- Make “low-text page” triage measurable.

Threshold (default)
- If > 20% of characters on a page are low-confidence (OCR engine confidence < 60), route page to manual coverage fix queue.
- Else: accept OCR output as derived layer.

Recording
- X1.manifest.extraction.parameters must include:
  - ocr_engine
  - ocr_confidence_threshold (=60)
  - low_confidence_pct_threshold (=0.20)
  - pages_flagged[]
