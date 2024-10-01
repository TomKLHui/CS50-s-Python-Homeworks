import inflect

def main():
    p = inflect.engine()
    names=rollcall("Name: ")
    print("Adieu, adieu, to", p.join(names))

def rollcall(n):
    namelist=[]
    while True:
        try:
            namelist+=[str.strip(input(n))]
        except KeyError:
            pass
        except EOFError:
            return namelist


main()