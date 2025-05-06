def numvowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    total = 0
    for i in word:
        if i in vowels:
            total = total + 1
        else:
            pass
    print (total)

user_word = str(input("Please enter a word: - "))

numvowels(user_word)