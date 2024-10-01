import os
import sys
from PIL import Image
from PIL import ImageOps

def main():
    check()
    wear()

def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    formats=[".jpg",".jpeg",".png"]
    if os.path.splitext(sys.argv[1])[1] not in formats or os.path.splitext(sys.argv[2])[1] not in formats :
        sys.exit("Invalid output")
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")

def wear():
    try:
        shirt = Image.open("shirt.png")
        before = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    size = shirt.size
    before = ImageOps.fit(before, size)
    before.paste(shirt, shirt)
    before.save(sys.argv[2])
if __name__ == "__main__":
    main()
