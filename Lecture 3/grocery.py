def main():
    order=grocery("")
    for i in order:
        print(order[i],i)

def grocery(food):
    Total={}
    while True:
        try:
            item=str.strip(input(food)).upper()
            if item in Total:
                Total[item]+=1
            else:
                Total[item]=1
        except KeyError:
            pass
        except EOFError:
            Total=dict(sorted(Total.items()))
            return Total


main()
