inventory = {
    "laptops" : 12,
    "iPads" : 8,
    "headphones" : 15
}

inventory["webcams"] = 6

inventory.pop("iPads")

print(inventory["laptops"])

for key, value in inventory.items():
    print(f"{key} - {value}")