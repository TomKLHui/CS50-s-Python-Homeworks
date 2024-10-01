from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
listfont=figlet.getFonts()
##Check sysarg (0/2)
if len(sys.argv)!=1 and len(sys.argv)!=3:
    sys.exit("Invalid usage")
##Check font validity and set font
if len(sys.argv)==1:
    figlet.setFont(font=random.choice(listfont))
elif len(sys.argv)==3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in listfont:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

##input
text=str.strip(input("Input:"))
print("Output:\n",figlet.renderText(text))
