from dataclasses import dataclass

@dataclass(frozen=True)
class Policy:
    min_test_coverage: float = 80.0
    high_financial_impact: float = 100000.0
    require_approval_for_pii: bool = True
    require_explanation_for_decisions: bool = True

DEFAULT_POLICY = Policy()
