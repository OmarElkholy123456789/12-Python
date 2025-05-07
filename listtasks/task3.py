items = []

while len(items) < 5:
    user_items = input("Please choose a grocery item - ")
    items.append(user_items)

print(items)

remove_items = input("Would you like to remove any items (yes/no) - ")

while True:
    if remove_items == "yes":
        item_removed = input("Which item would you like removed? - ")
        items.remove(item_removed)
        remove_items = input("Would you like to remove any items (yes/no) - ")
    elif remove_items == "no":
        print(f"Ok, here is your final list: {items}")
        break
    else:
        print("Please type yes or no.")