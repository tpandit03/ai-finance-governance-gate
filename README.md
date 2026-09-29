# AI Finance Governance Gate

A deterministic governance and validation gate for AI-generated financial workflows.

The system answers a practical enterprise question:

> **Can this AI-generated change move from development toward production?**

It evaluates a change request against explicit controls for security, data privacy, financial impact, tests, approvals, explainability, and auditability.

## Core idea

**AI-generated artifact → Governance Gate → Deterministic checks → Decision + Evidence**

The model is not allowed to grade its own work. The gate uses explicit policies and machine-verifiable evidence.

## Features

- Policy-as-code
- Risk scoring
- Deterministic validation
- Separation of duties
- Sensitive-data checks
- Required test evidence
- Financial-impact thresholds
- JSON audit report
- CLI
- Unit tests

## Run

```bash
python -m venv .venv
# activate it
pip install -r requirements.txt
python scripts/demo.py
pytest
```

## Example policy checks

| Control | Example |
|---|---|
| Security | No secrets in generated files |
| Data | PII access requires approval |
| Testing | Minimum unit-test evidence |
| Financial risk | High-impact changes require additional approval |
| Explainability | Automated financial decisions need explanation |
| Audit | Every gate decision produces evidence |

## Disclaimer

This is a portfolio reference architecture. It is not a legal or regulatory compliance certification.
