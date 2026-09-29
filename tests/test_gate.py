from src.gate import run_gate

def base():
    return {
        "change_id": "TEST-1",
        "test_coverage": 90,
        "contains_secrets": False,
        "uses_pii": False,
        "pii_approval": False,
        "financial_impact": 1000,
        "risk_approval": False,
        "automated_financial_decision": False,
        "explanation_available": False,
    }

def test_pass():
    result = run_gate(base())
    assert result["decision"] == "PASS"

def test_low_coverage_blocks():
    x = base()
    x["test_coverage"] = 50
    assert run_gate(x)["decision"] == "BLOCK"

def test_secret_blocks():
    x = base()
    x["contains_secrets"] = True
    assert run_gate(x)["decision"] == "BLOCK"

def test_high_impact_requires_approval():
    x = base()
    x["financial_impact"] = 500000
    assert run_gate(x)["decision"] == "BLOCK"
    x["risk_approval"] = True
    assert run_gate(x)["decision"] == "PASS"

def test_pii_requires_approval():
    x = base()
    x["uses_pii"] = True
    assert run_gate(x)["decision"] == "BLOCK"
    x["pii_approval"] = True
    assert run_gate(x)["decision"] == "PASS"
