import re  # Import regex module

# Take name input and remove extra whitespace
name = input("What's your name? ").strip()

# := is the "walrus operator" — assigns AND checks in one line
# re.search() returns a match object if pattern found, else None
# Pattern breakdown: r"^(.+), *(.+)$"
# ^     — start of string
# (.+)  — GROUP 1: one or more chars (captures Last name)
# ,     — literal comma must be present
# ' *'  — zero or more spaces after comma
# (.+)  — GROUP 2: one or more chars (captures First name)
# $     — end of string
if matches := re.search(r"^(.+), *(.+)$", name):

    # matches.group(0) — entire match
    # matches.group(1) — first  () group → Last name  e.g. "Malan"
    # matches.group(2) — second () group → First name e.g. "David"
    name = matches.group(2) + " " + matches.group(1)
    # Rearranges: "Malan, David" → "David Malan"

print(f"hello, {name}") 