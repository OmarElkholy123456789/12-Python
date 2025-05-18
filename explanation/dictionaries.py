# Creating a student dictionary

student = {
    "name" : "Elvin",
    "age" : 16,
    "fav subject" : "Geography",
    "licence" : "none, not even learners"
}

# Print the entire dictionary
print(student)

#Print certain values of the dictionary
print(student["name"])
print(student["licence"])

print(student.get("age"))

# Update a value
student["fav subject"] = "waiting to long"

# Add a new value
student["Email"] = "elvinlicence@gmail.com"

# Delete a value
student.pop("licence")

print(student)

# Run through my dictionary

for key in student:
    print(f"{key} - {student[key]}")

# or

# Looping through your dictionary is best with this loop, as you declare
# two different values i your for loop with one assigned to your key
# and the other assigned to the keys values

for key, value in student.items():
    print(f"{key} - {value}")