from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from .policy import Policy, DEFAULT_POLICY

@dataclass
class Check:
    name: str
    passed: bool
    severity: str
    evidence: str

def run_gate(change: dict, policy: Policy = DEFAULT_POLICY) -> dict:
    checks = []

    tests = float(change.get("test_coverage", 0))
    checks.append(Check(
        "TEST_COVERAGE",
        tests >= policy.min_test_coverage,
        "HIGH",
        f"coverage={tests:.1f}%, required>={policy.min_test_coverage:.1f}%"
    ))

    secrets = int(change.get("contains_secrets", False))
    checks.append(Check(
        "SECRET_SCAN",
        secrets == 0,
        "CRITICAL",
        "No hard-coded secrets detected" if secrets == 0 else "Potential secret detected"
    ))

    pii = int(change.get("uses_pii", False))
    approval = int(change.get("pii_approval", False))
    pii_pass = (not pii) or (not policy.require_approval_for_pii) or bool(approval)
    checks.append(Check(
        "PII_APPROVAL",
        pii_pass,
        "CRITICAL",
        f"uses_pii={bool(pii)}, approval={bool(approval)}"
    ))

    impact = float(change.get("financial_impact", 0))
    impact_ok = impact < policy.high_financial_impact or bool(change.get("risk_approval", False))
    checks.append(Check(
        "FINANCIAL_IMPACT",
        impact_ok,
        "HIGH",
        f"impact=${impact:,.2f}, approval={bool(change.get('risk_approval', False))}"
    ))

    decision = int(change.get("automated_financial_decision", False))
    explanation = int(change.get("explanation_available", False))
    explain_ok = (not decision) or (not policy.require_explanation_for_decisions) or bool(explanation)
    checks.append(Check(
        "EXPLAINABILITY",
        explain_ok,
        "HIGH",
        f"automated_decision={bool(decision)}, explanation={bool(explanation)}"
    ))

    passed = all(c.passed for c in checks)
    return {
        "change_id": change.get("change_id", "UNKNOWN"),
        "decision": "PASS" if passed else "BLOCK",
        "checks": [asdict(c) for c in checks],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
