def main():
    var=input("camelCase:")
    snek=snakify(var)
    print(snek)

def snakify(camel):
    chopped=[c for c in camel]
    graft=[]
    for letter in chopped:
        if letter.isupper()==True:
            graft.append("_")
        graft.append(str.lower(letter))
    rejoined="".join(graft)
    return rejoined

main()
