def main():
    mass= input("Mass (kg) in integers:")
    atomic(mass)

def atomic(MASS):
    c= 300000000
    E= int(MASS)*(c**2)
    print("Energy (Joules):",E)

main()
