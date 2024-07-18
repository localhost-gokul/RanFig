from pyfiglet import figlet_format
from random import randint

number = randint(1,60)
number = str(number)
letter = figlet_format(number, font="doh")

print(letter)