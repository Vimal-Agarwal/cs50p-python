"""# while loop
i = 0
while i<3:
    print("Hello!, while")
    i +=1

# for loop with list in python
for i in [0, 1, 2]:
    print("Hello!!, for")

# use of range keyword for list in many iteration need
for i in range(3):     # we can also use inplace of i varible _ because i is not repeat and use.
    print("Hello!!")

print ("meow \n" * 3) # pythonic way 
"""

while True:
    n = int(input("enter the value of n: "))
    if n>0:
        break


for _ in range(n):
    print ("Hello!!")
