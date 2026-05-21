# exception handling
try:
    x=int(input("enter the x: "))
except ValueError:
    print("x is not a integer.")
else:                            # else use for NameError
    print(f"x is {x}")


# pass keyword use to pass without distrub code or just go forward in exception the Value Error