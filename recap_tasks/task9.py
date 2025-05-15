import easygui

name = easygui.enterbox("What is you name?")

num = easygui.integerbox("Please choose the number of times you would " \
"like your name to be repeated:")

number = []

for i in range(1, num + 1):
    number.append(name)

easygui.msgbox(number)