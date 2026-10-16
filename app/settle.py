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

def settle(balances):
    """Turn balances into a list of payments that settles everyone up.

    balances: dict {member_id: balance_cents}. The values must add up to 0.
    Returns a list of (from_member, to_member, amount_cents) tuples.
    """
    balances = dict(balances)  # work on a copy, so we don't change the caller's dict
    payments = []

    while True:
        # creditor = the member with the BIGGEST balance
        creditor = None #set the creditor to be no one
        for member in balances: #for each member in the balances dict
            if creditor is None or balances[member] > balances[creditor]: #we use this if statement to stet the creditor
                creditor = member
        # debtor = the member with the SMALLEST balance
        debtor = None
        for member in balances:
            if debtor is None or balances[member] < balances [debtor]:
                debtor = member
        # if the creditor's balance is 0, everyone is settled, so stop
        if balances[creditor] == 0:
            break
        # amount = the smaller of (what the creditor is owed, what the debtor owes)
        amount = min(balances[creditor], -balances[debtor])
        # record the payment: (debtor, creditor, amount)
        payments.append((debtor, creditor, amount))
        # update both balances
        balances[creditor] -= amount
        balances[debtor] += amount
        

    return payments