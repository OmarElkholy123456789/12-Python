import easygui

num_of_items = 0

items = []

while num_of_items < 5:
    user_items = easygui.enterbox("Please choose your 5 items:")
    num_of_items += 1
    items.append(user_items)

easygui.msgbox(f"You item list: {items}")