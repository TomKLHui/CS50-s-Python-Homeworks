def main():
    var=input("Input:")
    uwu=shorten(var)
    print("Output:",uwu)

def shorten(camel):
    chopped=[c for c in camel]
    graft=[]
    for letter in chopped:
        if letter not in ["A","a","E","e","I","i","O","o","U","u"]:
            graft.append(letter)
    rejoined="".join(graft)
    return rejoined

if __name__ == "__main__":
    main()
