def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6 :
        return False
    elif s[0:2].isalpha()==False:
        return False
    elif len(s)>2 and s[2]=="0":
        return False
    elif s.isalpha()==False and s[-1].isalpha():
        return False
    elif s.isalnum()==False:
        return False
    for l in range(1,len(s)):
        if s[l].isalpha() and s[l-1].isnumeric():
            return False
    return True

if __name__ == "__main__":
    main()
