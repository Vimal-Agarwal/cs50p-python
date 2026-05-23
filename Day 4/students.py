import csv  # Import built-in CSV module to read .csv files

students = []  # Empty list to store all student records

with open("students.csv") as file:  # Open the CSV file (auto-closes after block)
    reader = csv.reader(file)        # Create a reader object to parse the file
    for name, home in reader:        # Unpack each row into 'name' and 'home'
        students.append({"name": name, "home": home})  # Store as dict in list

# Sort the list alphabetically by "name" field using lambda as the key
for student in sorted(students, key=lambda student: student["name"]):
    # Print each student's name and hometown using f-string formatting
    print(f"{student['name']} is from {student['home']}")