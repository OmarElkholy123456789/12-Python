# Nested Dictionaries

students = {
    "Elvin" : {
        "Age" : 16,
        "Subjects" : ["DTP", "ENGE", "MACE", "GEOE", "PHYE", "CHEE"],
        "Student ID" : 22360
    },
    "Xavier" : {
        "Age" : 32,
        "Subjects" : ["DTP", "ENGE", "ECOE", "PHYE", "HISE", "MAC"],
        "Student ID" : 22135
    },
    "Mr Douglas" : {
        "Age" : 28,
        "Subjects" : ["9DTC", "10DTC", "11DTP", "12DTP"],
        "Student ID" : 00000
    }
}

print(students["Xavier"]["Age"])

for student, key, value in students.items():
    print(f"{student}: {key["Age"]}")

# Add a new student to the school

students["Tomas"] = {
    "Age" : 16,
    "Subjects" : ["DTP", "PED", "MAC", "MAS", "ENG", "ECO"],
    "Student ID" : "22389"
}