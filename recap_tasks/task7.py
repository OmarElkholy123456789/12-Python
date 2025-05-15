import easygui

num = easygui.integerbox("Please choose a number:")

multiplied_nums = []

for i in range(1, 11):
    multiplied_nums.append(num*i)

easygui.msgbox(multiplied_nums)