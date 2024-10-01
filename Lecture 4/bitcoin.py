import json
import requests
import sys

def main():
    if len(sys.argv)!=2:
        sys.exit("Missing command line argument")
    try:
        btc=float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
    try:
        curr_price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        sys.exit("Connection Error?")
    total= btc*curr_price["bpi"]["USD"]["rate_float"]
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
