from app.settle import compute_balances

EXPENSES = [
    {"id": 1, "paid_by": 1, "amount_cents": 9000},  # Alex paid for dinner
    {"id": 2, "paid_by": 2, "amount_cents": 6000},  # Bea paid for gas
]
SPLITS = [
    {"expense_id": 1, "member_id": 1, "share_cents": 3000},
    {"expense_id": 1, "member_id": 2, "share_cents": 3000},
    {"expense_id": 1, "member_id": 3, "share_cents": 3000},
    {"expense_id": 2, "member_id": 2, "share_cents": 3000},
    {"expense_id": 2, "member_id": 3, "share_cents": 3000},
]


def test_banff_balances():
    assert compute_balances(EXPENSES, SPLITS) == {1: 6000, 2: 0, 3: -6000}


def test_balances_sum_to_zero():
    assert sum(compute_balances(EXPENSES, SPLITS).values()) == 0


def test_no_expenses():
    assert compute_balances([], []) == {}