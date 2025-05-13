sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequency:")
for word in frequency:
    print(word + ":", frequency[word])