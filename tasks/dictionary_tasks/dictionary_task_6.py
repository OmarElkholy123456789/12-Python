grades = {
    "Xavier" : 32,
    "Elvin" : 81,
    "Omar" : 77,
    "Brent" : 68,
    "Demitri" : 89
}

for key, value in grades.items():
    if value > 80:
        print(f"{key} - {value}")