def main():
    greeting=input("Greeting: ")
    money=value(greeting)
    print(f"${money}")
def value(GREETING):
    formatted=str.strip(GREETING).lower()
    if formatted[:5]=="hello":
        return 0
    elif formatted[:1]=="h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

