"""Settle-up math. Pure functions: no database, no web, just data in, data out."""


def compute_balances(expenses, splits):
    """Return each member's net balance in cents.

    expenses: list of dicts like {"id": 1, "paid_by": 1, "amount_cents": 9000}
    splits:   list of dicts like {"expense_id": 1, "member_id": 1, "share_cents": 3000}

    Returns a dict {member_id: balance_cents}.
    Positive = others owe them. Negative = they owe others.
    """
    balances = {}

    #loop over expenses, ADD amount_cents to the payer's balance
    for expense in expenses: #for each expense in expenses
        payer = expense["paid_by"] #get the id for the person who paid
        amount = expense["amount_cents"] #get the amount they paid
        balances[payer] = balances.get(payer, 0) + amount #look up this persons total so far; if they have no balance start at 0 iand save the new total under their id
 
    # loop over splits, SUBTRACT share_cents from that member's balance
    # Go through the splits one at a time (each is one person's share of one expense).
    for split in splits:
        member = split["member_id"]     # who owes this share
        amount = split["share_cents"]   # how much they owe, in cents
        balances[member] = balances.get(member, 0) - amount   # subtract it from their total

    return balances