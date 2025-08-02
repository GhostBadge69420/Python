txt_data = "I like pizza"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path} was created'")

# w = is for write
# x = is to write a file if that file doesn't already exist
# a = to append