import csv

with open("Student.csv", "r") as file:

    reader = csv.reader(file)
    
    next(reader)  # Skip header row
    
    for row in reader:
        name = row[0]
        status = row[2]
        
        if status == "Pass":
            print(name)

