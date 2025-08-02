import json

Resturant = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "Resturant.json"

try:
    with open(file_path, "w") as file:
        json.dump(Resturant, file, indent=4)
        print(f"json file '{file_path}' was created ")
except FileExistsError:
    print("That file already exists!")