txt_data = "I like pizza!"

file_path = "output.txt"

try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")