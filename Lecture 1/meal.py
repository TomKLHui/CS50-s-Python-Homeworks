def main():
    time = input("What time is it?")
    time = convert(time)
    if 7.0<=time<=8.0:
        print("breakfast time")
    elif 12.0<=time<=13.0:
        print("lunch time")
    elif 18.0<=time<=19.0:
        print("dinner time")

def convert(TIME):
    hours,minutes=str.strip(TIME).split(sep=":")
    hours=int(hours)
    minutes=float(minutes)/60
    return hours+minutes

if __name__ == "__main__":
    main()
