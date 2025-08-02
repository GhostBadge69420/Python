import csv

clients = [["Name", "Age", "Job"],
           ["Sergy", 38, "Entrepreneur"],
           ["Wallace", 41, "Singer"],
           ["John", 34, "CEO"]]

file_path = "clients.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in clients:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")