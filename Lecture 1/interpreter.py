def main():
    formula=input("Expression: ")
    print(calc(formula))

def calc(FORMULA):
    x, y ,z=str.strip(FORMULA).split(sep=" ")
    if y == "+":
        return round(float(x)+float(z),1)
    elif y == "-":
        return round(float(x)-float(z),1)
    elif y == "*":
        return round(float(x)*float(z),1)
    elif y == "/":
        return round(float(x)/float(z),1)
    else:
        return "Error"
main()

