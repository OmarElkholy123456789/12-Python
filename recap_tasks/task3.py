import easygui

password = "xavierdidntmakeit"

user_input = easygui.enterbox("Enter password:") 

while True:
    if user_input == password:
        easygui.msgbox("Acces granted.")
        break
    else:
        user_input = easygui.enterbox("Incorrect password. Please try again:")