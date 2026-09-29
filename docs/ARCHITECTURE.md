# Architecture

```text
 AI-generated change
        |
        v
 +-------------------+
 | Evidence Collector|
 +---------+---------+
           |
           v
 +-------------------+
 | Policy-as-Code    |
 +---------+---------+
           |
    +------+------+
    |             |
    v             v
Security       Financial
Checks         Risk Checks
    |             |
    +------+------+
           |
           v
 +-------------------+
 | Deterministic Gate|
 +---------+---------+
           |
      PASS / BLOCK
           |
           v
     Audit Evidence
```

## Key design principle

The AI system can propose code or workflow changes, but it does not get authority to certify its own correctness. Independent deterministic controls produce the release decision.

## Production extensions

- GitHub Actions integration
- SAST/secret scanning
- SBOM and dependency policy
- OPA/Rego policy engine
- Evidence stored in immutable audit storage
- Risk-tiered approval workflows
- OpenTelemetry traces
- Model and prompt versioning
- Signed artifacts
