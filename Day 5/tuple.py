# Tuple is immutable collection which mean Cannot change values after creation.
# list is mutable which mean change values after creation.
def main():
    student = get_student()                   # stores the returned tuple in 'student'
    print(f"{student[0]} from {student[1]}")  # access tuple elements by index (starts from 0)

# Collects user input and returns it as a tuple
def get_student():
    name = input("Name: ")    # take name from user
    house = input("House: ")  # take house from user
    return (name, house)      # pack both values into a tuple in () and return

# Ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()