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

5.
user_input = ""

while True:
    user_input = str(input("Please type yes")).strip().lower()
    if user_input == "yes":
        print ("Good sole")
        break

6.
for i in range (11):
    print(i)


7.
movie_list = ["Interstellar", "Shutter Island", "Inception"]

for movie_name in movie_list:
    print(movie_name)


8.
numbers = [2, 5, 3]
total = 0

for num in numbers:
    total = total + num

print (total)

9.
import random

numb = random.randint(1, 10)

while True:
    try:
        user_input = int(input("Please pick a number from 1-10"))
        if user_input == numb:
            print ("You got it!")
            break
        else:
            print ("Wrong! Try again.")
    except:
        ValueError
        print ("Incorrect value.")

10.
print ("1. Start Game")
print ("2. Load Game")
print ("3. Quit")

user_input = int(input("Please choose an option:    "))
if user_input == 1:
    print ("The game is starting now.")
elif user_input == 2:
    print ("Loading the game now.")
elif user_input == 3:
    print("Quitting now.")
else:
    print("Please pick one of the options from 1-3")

11.
animals = ["dog", "cat", "bird", "horse", "zebra"]
user_input = input("What is your favourite animal?").lower()
check = False

for i in animals:
    if i == user_input:
        print("Your animal is in the list.")
        check = True
    else:
        pass

if check == False:
    print("That animal is not in the list.")

12.
user_input = int(input("Please enter a number.  "))

for i in range (user_input, -1, -1):
    print(i)

13.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    if i % 2 == 0:
        print (i)

        
14.
user_pass = str(input("Please create a password.    "))

user_input = str(input("Please enter your password. "))

while user_input != user_pass:
    print("Access denied.")
    user_input = str(input("Please enter your password. "))
    if user_input == user_pass:
        print("Access granted.")
        break

    """