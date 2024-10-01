import random
import sys

def main():
    while True:
        try:
            lvl=int(input("Level:"))
            if lvl <1:
                pass
            else:
                break
        except ValueError:
            pass

    game(lvl)

def game(level):
    ans=random.randint(1,level)
    while True:
        try:
            guess=int(input("Guess:"))
            if guess <1:
                pass
            elif guess <ans:
                print("Too small!")
            elif guess>ans:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass
main()
