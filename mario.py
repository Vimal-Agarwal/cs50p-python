# making a 2-d box like matrix in c.
def main():
    n = int(input("Enter the value of n: "))
    print_square(n)

""" this is like a 2-d matrix in c.
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
"""

# shoter way of above code 
def print_square(size):
    for i in range(size):
        print("#" * size)

main()