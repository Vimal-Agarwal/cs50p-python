# 3. sys library
import sys

"""
print("hello, my name is: ", sys.argv[1])  # this give error because at index 1 we need to pass one argumenet with pytho library.py , So to handle this indexerror (IndexError: list index out of range) we use conditional statements.
"""

if len(sys.argv) < 2:
    print("To few argument")
elif len(sys.argv) > 2:
    print("To many argumenets")
else:
    print("Hello, my name is: ", sys.argv[1])

# we can also use sys.exit for write our main code effectively.
# sys.exit use to exit the code when conditions are true.
if len(sys.argv) < 2:
    sys.exit("To few argument")
elif len(sys.argv) > 2:
    sys.exit("To many argumenets")

print("Hello, my name is: ", sys.argv[1])


# slice is a subset of data structure like a list. means when we write a for loop to above similar program then file name also come in output but by using slice method we make a perfect output

if len(sys.argv) < 2:
    sys.exit("To few argument")
for arg in sys.argv[1:]:              # [1:] mean a slice which start with index 1 to end.
    print("Hello, my name is: ", arg)
