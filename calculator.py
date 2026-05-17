# Topic: Arithmetic, f-strings, Rounding

x = float(input("What's x? "))
y = float(input("What's y? "))

"""
z = int(x) + int(y)
z = float(x) + float(y)
"""
z = x +y
print(z)

# use round for rounding the number with written in number system format by using 'f'
z = round(x+y)
print(f"{z:,}")