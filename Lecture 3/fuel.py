def main():
    percentfuel=convert(input("Fraction:"))
    print(gauge(percentfuel))

def convert(fraction):
    while True:
        try:
            X,Y=str.strip(fraction).split(sep="/")
            percent= round(int(X)/int(Y)*100)
            if 0<=percent<=100:
                return percent
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return str(percentage)+"%"

if __name__ == "__main__":
    main()
