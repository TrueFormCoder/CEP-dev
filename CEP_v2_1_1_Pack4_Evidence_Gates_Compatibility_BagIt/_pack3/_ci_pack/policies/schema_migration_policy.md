CEP Schema Migration Policy (v2.1.1)

Definitions
- Additive change: adds optional fields, new enums that do not invalidate existing artifacts, relaxed constraints.
- Breaking change: changes required fields, tightens patterns, removes enums/fields, or changes const schema_version.

Rules
1) Additive-only changes MAY keep schema_version constant.
2) Any breaking change MUST bump schema_version const and $id urn version.
3) Delta Mode (X3) MUST compare runs only if schema_version is compatible.

Compatibility Check
- Compatible if:
  - identical schema_version, OR
  - explicitly allowed via a compatibility map file (future).
