def checker(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

user_str1 = str(input("Please choose your first string."))
user_str2 = str(input("Please choose your second string."))

print(checker(user_str1, user_str2))