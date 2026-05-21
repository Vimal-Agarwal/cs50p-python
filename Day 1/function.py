# Topic: User-defined Functions, def keyword

# user-defined function is write with 'def' keyword which mean define.

def main():
    x = int(input("What's x? "))
    print("x squared is",square(x))

def square(n):
    return n*n

main()