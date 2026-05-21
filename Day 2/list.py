# list is similar to array in c

students = ["Harry", "Harmione", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])


# dict is dictionary keyword in python, it means dictionary use in real life to dictate the word by a alphabet
students = { # {use for dictionary}
    "Harry" : "Gryffindor",
    "Hermione" : "Gryffindore",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",

}
for student in students:
    print(student, students[student], sep=",")


# example of list and dictionary
students = [
    {"name":"Vimal", "age":"twenty", "city":"jaipur"}, #this is dictionary in which get values on basis of key like name, age, city.
    {"name":"Jatin", "age":"twenty", "city":"jaipur"},
    {"name":"Gajju", "age":"twenty", "city":None} # None is a special keyword use for null value in python
]

for student in students:
    print(student["name"], student["age"], student["city"], sep=", ")
