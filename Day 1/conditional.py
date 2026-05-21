# Topic: if/else, Boolean Expressions, Functions

def main():
    x = int(input("enter the value of x: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    return n%2==0

# return True if n%2==0 else False

""" 
if n%2==0:
        return True
    else:
        return False  
"""
    
main()

"""
y = int(input("enter the value of y: "))

if x>y:
    print("x is greater")

elif x<y :
    print("x is smaller")

else :
    print("both are equal")
"""
"""
if x>y or x<y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""

"""
if x>y and x<y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""