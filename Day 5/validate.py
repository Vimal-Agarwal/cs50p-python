# Regular Expressions (regex) 

import re  # Import regex module for pattern matching

# Take email input from user and remove extra spaces from both ends
email = input("What's your email? ").strip()

# re.search() scans the string for a match to the pattern
# r"..." — raw string so backslashes are treated literally
# ^ — string must START here
# .+ — one or more of any character (username part)
# @ — literal @ symbol must be present
# .+ — one or more of any character (domain name)
# \. — literal dot (escaped, not "any character")
# edu — must literally end with "edu"
# $ — string must END here
# So username and domain can't contain extra @ symbols
# [^@\.]+ means "any character EXCEPT @ and dot"
# This ensures clean username and domain with no extra dots/@ symbols
# re.IGNORECASE is a flag which use to ignore lower and uppercase of input.
if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.edu$", email, re.IGNORECASE):   # [a-zA-Z0-9] insted of use this we can write \w
    print("Valid")    
else:
    print("Invalid")
