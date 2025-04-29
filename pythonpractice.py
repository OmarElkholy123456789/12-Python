"""
1. 
print("Hello, my name is Omar, I like to play games, I like pizza.")

2.
name = input("What is your name?")
age = input(f"Nice to meet you {name}, how old are you?")

print(f"That's cool {name}, I am also {age} years old")

3.
numb = int(input("Pick a number. I'll tell you if it is even or odd."))

if numb % 2 == 0:
    print("Even.")
else:
    print("Odd.")

4.
numb = input("Choose a number from 1 to 3")

if numb == 1:
    print("You chose apple!")
elif numb == 2:
    print("You chose banana!")
elif numb == 3:
    print ("You chose cherry")
else:
    print("That isn't a number from 1 to 3")

"""

check = False

while check == False:
    user_input = str(input("Please type 'yes'")).lower
    if user_input == "yes":
        print("Thanks")
        check = True
