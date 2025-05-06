numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def indentifier(num):
    biggest = 0
    for i in num:
        if i > biggest:
            biggest = i
        else:
            pass
    print(biggest)

indentifier(numbers)