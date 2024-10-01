import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"^(\d|1[012]):?(\d{2})? ([AP])M to (\d|1[012]):?(\d{2})? ([AP])M$",s)
    if matches:
        start_h=int(matches.group(1))
        start_m=int(matches.group(2) if matches.group(2) else 0)
        start_ap=matches.group(3)
        end_h=int(matches.group(4))
        end_m=int(matches.group(5) if matches.group(5) else 0)
        end_ap=matches.group(6)
        if start_m>59 or end_m>59 or start_h>12 or end_h>12:
            raise ValueError
        start=convert24(start_h,start_m,start_ap)
        end=convert24(end_h,end_m,end_ap)
        return f"{start} to {end}"
    else: raise ValueError

def convert24(h,m,ap):
    if ap == "A" and h== 12:
        h=0
    if ap == "P" and h< 12:
        h+=12
    return f"{h:02}:{m:02}"

if __name__ == "__main__":
    main()
