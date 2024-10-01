from datetime import date,datetime
import re
import inflect
import sys

def main():
    birthdate=input("Date of Birth:")
    if validate(birthdate) == False:
        sys.exit("Invalid date")
    print(convert_minutes(birthdate))

def validate(ip):
    try:
        datetime.strptime(ip, "%Y-%m-%d")
    except ValueError:
        return False
    return True
def convert_minutes(birthdate):
    today=date.today()
    timedelta=today-date.fromisoformat(birthdate)
    minutes=int(round(timedelta.total_seconds()/60,0))
    word = inflect.engine().number_to_words(minutes, andword = '').capitalize() + " minutes"
    return word

if __name__ == "__main__":
    main()
