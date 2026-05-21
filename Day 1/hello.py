# Topic: User Input, String Methods

print("what's your name?")

# Single line comment by '#' & Multiline comments by """Multilines"""
# To get user Input we use 'input()'
# use of Variables
name = input()

print("hello, " + name) # single argument we use '+' 
# print("hello,", name) this is also same but we pass one or more arguments with , use

# Remove whitespaces from str
name = name.strip()

# Capitalize str
name = name.capitalize() #use to capitalize only fist letter
name = name.title()      #use to capitalize all first letter 

# We can also use both strip and title in one line
# name = name.strip().title() 
print("hello," , name)

