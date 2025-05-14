import easygui

user_weather = easygui.choicebox("What is your weather like? :", 
                                 choices = ["sunny", "rainy", "windy"])

if user_weather == "sunny":
    easygui.msgbox("Go outside")
elif user_weather == "rainy":
    easygui.msgbox("Stay inside")
else:
    easygui.msgbox("hgdjfhgkdg") 