# File I/O

name = input("what's your name? ")

file = open("names.txt", "a")  # a is use for append text.
file.write(f"{name}\n")
file.close()