# Class = Blueprint / Template for creating objects
# Just like a "Student Form" — defines what fields a student has
class Student:
    # __init__ METHOD (Constructor)
    # Automatically called when a new Student object is created
    # "self" refers to the current object being created
    # Parameters: name and house are passed during object creation
    def __init__(self, name, house):

        # Validate name — if empty, raise error
        if not name:
            raise ValueError("Name cannot be empty!") #raise is used to manually throw an error
        
        # Validate house — only specific houses allowed
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house!")

        self.name = name      # store name as object attribute
        self.house = house    # store house as object attribute
        # self.name and self.house belong to THIS specific object
        # Every student object will have its OWN name and house]

    def __str__(self):  # __str__ is the method Python calls automatically whenever you do print(object).
        return f"{self.name} from {self.house}"


def main():
    # get_student() returns a Student OBJECT
    student = get_student()

    # Accessing object attributes using DOT (.) notation
    # print(f"{student.name} from {student.house}")
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")

    # Creating a NEW Student object using the class blueprint
    # Student(name, house) calls __init__ construtor automatically
    student = Student(name, house)

    # Returning the full object (not just a tuple or string)
    return student

if __name__ == "__main__":
    main()