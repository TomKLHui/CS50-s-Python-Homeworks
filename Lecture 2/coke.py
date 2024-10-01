due = 50

while due > 0:
    print("Amount Due:",due)
    coin= int(input("Insert Coin:"))
    accepted=[5,10,25]
    if coin in accepted:
        due=due-coin
print("Change Owed:", due*-1)
