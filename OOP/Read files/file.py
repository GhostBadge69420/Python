file_path = "employee.txt"

with open(file_path, "r") as file: # r = read
    content = file.read()
    print(content)