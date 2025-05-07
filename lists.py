fruits = ["Apple", "Mandarin", "Banana", "Tomato", "Grape", "Cherry", 
          "Orange", "Date", "Fig", "Pear", "Pommegranate", "Grapefruit"]

# Each item of our list has its own unique number
# The first item in our list has an index value of 0 - Apple is 0
# Grapefruit is our final item but it has an index value of 11

# Print fruit list
print(fruits)

# Print a certain item from the list
print(fruits[6])

# Remove an item from the list
fruits.remove("Cherry")

#Add an item to the list
fruits.append("Starfruit")

# Print the updated list
print(fruits)

#Print the length of my list
print(len(fruits))