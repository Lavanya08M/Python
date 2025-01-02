from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    is_random = True
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
    is_random = False
else:
    sys.exit("Invalid usage")

if not is_random:
    figlet.setFont(font=sys.argv[2])
else:
    figlet.setFont(font=random.choice(fonts))

text = input("Input: ")
print("Output:")
print(figlet.renderText(text))





