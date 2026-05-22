# File I/O

#name = input("what's your name? ")

"""
file = open("names.txt", "a")  # a is use for append text.
file.write(f"{name}\n")
file.close()
"""

# to make pythonic file manuplating we use with keyword instead of close.

"""with open("names.txt", "a") as file:
    file.write(f"{name}\n")"""

# read existing file
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())


# sorted reading of existing file
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
