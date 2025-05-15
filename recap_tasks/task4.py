import easygui

user_age = int(easygui.enterbox("How old are you? "))

while True:
    if user_age >= 0 and user_age <= 12:
        easygui.msgbox("You are a child.")
        break
    elif user_age >= 13 and user_age <= 17:
        easygui.msgbox("You are a teen.")
        break
    elif user_age >= 18 and user_age <= 80:
        easygui.msgbox("You are an adult.")
        break
    else:
        user_age = int(easygui.enterbox("Please enter your real age: "))