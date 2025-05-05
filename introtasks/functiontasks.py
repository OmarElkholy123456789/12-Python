"""

1.
def greet_user(name):
    print(name)

user_input = input("What is your name?")
greet_user(user_input)


2.
def check_even_odd(num):
    if num % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

number = int(input("Chose a number and I will tell you if it is even or odd."))
check_even_odd(number)

3.
def multiplication_table(num):
    for x in range(13):
        print(num * x)

number = int(input("Please pick any number. "))

multiplication_table(number)

"""
num = int(input("please pick a positive number:   "))

def sum_of_numbers(n):
    y = 0
    for x in range(1, n):
        y = y + x
        return y

print(sum_of_numbers(num))