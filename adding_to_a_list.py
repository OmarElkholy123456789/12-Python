# Creating a program which adds names to a list and then chooses a
# random winnder

import random

names = []

name = ""

while name != "Done":
    name = input("Please enter a name. Type 'Done' when you are finished - ")

    if name == "Done":
        break
    else:
        names.append(name)
        print(names)

winner = random.choice(names)
print(f"The winner is {winner}")