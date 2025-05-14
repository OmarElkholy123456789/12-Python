import easygui

grade = int(easygui.enterbox("Enter grade:"))

if grade >= 80 and grade <= 100:
    print("You got an excellence.")
elif grade >= 60 and grade <=79:
    print("You got a merit.")
elif grade >= 50 and grade <=59:
    print("You got an achieved.")
else:
    print("You got a not achieved.")