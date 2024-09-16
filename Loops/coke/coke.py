accepted_coins = [5, 10, 25]

amount_due = 50

while amount_due > 0:
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        amount_due -= coin
        print(f"Amount Due: {amount_due}")
    else:
        print(f"Amount Due: {amount_due}")
if amount_due < 0:
    print(f"Change Owed: {abs(amount_due)}")
else:
    print(f"Change Owed: 0")


