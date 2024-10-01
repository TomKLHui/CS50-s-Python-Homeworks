def main():
    POKER=input()
    emotional(POKER)

def emotional(TEXT):
    print(str.strip(TEXT).replace(":)","🙂").replace(":(","🙁"))

main()
