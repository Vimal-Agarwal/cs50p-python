# Topic: Match-Case (Python's switch statement, introduced in Python 3.10)

# match is similar to switch in c++

name = input("Enter your name: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                   # default case
        print("Who?")