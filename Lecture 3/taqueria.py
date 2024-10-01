menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
def main():
    order=bill("Item: ")
    print("\nGrand Total: $",str(format(order,".2f")),sep="")
def bill(food):
    Total=0
    while True:
        try:
            item=str.strip(input(food)).title()
            if item in menu:
                Total+=menu[item]
                print("$",str(format(Total,".2f")),sep="")
        except KeyError:
            pass
        except EOFError:
            return Total


main()
