import json
from src.gate import run_gate

examples = [
    {
        "change_id": "FIN-001",
        "test_coverage": 92,
        "contains_secrets": False,
        "uses_pii": False,
        "pii_approval": False,
        "financial_impact": 25000,
        "risk_approval": False,
        "automated_financial_decision": True,
        "explanation_available": True,
    },
    {
        "change_id": "FIN-002",
        "test_coverage": 61,
        "contains_secrets": False,
        "uses_pii": True,
        "pii_approval": False,
        "financial_impact": 250000,
        "risk_approval": False,
        "automated_financial_decision": True,
        "explanation_available": False,
    }
]
for example in examples:
    print(json.dumps(run_gate(example), indent=2))
