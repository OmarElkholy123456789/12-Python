import easygui

num = 7

user_input = easygui.integerbox("Make your guess:", lowerbound=0, \
upperbound=10)

while True:
    if user_input == num:
        easygui.msgbox("Correct!")
        break
    else:
        user_input = easygui.integerbox("Try again:", lowerbound=0, \
        upperbound=10)