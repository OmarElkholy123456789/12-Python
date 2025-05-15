import easygui

num = easygui.integerbox("Please choose a number")

sum = 0

for i in range(1, (num + 1)):
    sum = sum + i

easygui.msgbox(sum)