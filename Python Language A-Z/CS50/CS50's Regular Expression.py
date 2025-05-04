import re

#For email address validation
def mail():
    email = input("What's your email? ").strip()

    if re.search(r"^\w+@(\w|\.)+\.edu$", email, re.IGNORECASE):     # '\w' is alternative to [a-zA-Z0-9_]  and '|' is the OR operator -- and -- r"string" is called raw string -- and -- "^...$" to match the exact string -- and -- "\." the backslash is used because "." is to define any character not only dot in regular expressions.
        print("Valid")
    else:
        print("Invalid")




#For name validation
def full_name():
    name = input("What's your name? ")  #Example: David Malan, or (Malan, David)

    if matches := re.search(r"^(.+) *, *(.+)$", name):    #Walrus operator ":=" , The expression a := b is known as the "walrus operator" in Python. It assigns the value of b to a and returns the value of b. This operator is useful for assignments within expressions.
        name = f"{matches.group(2)} {matches.group(1)}"     #Capturing groups by parenthesis () from re.search
    print(f"Hello, {name}")





#Finding twitter username
def twitter():
    url = input("URL: ").strip()
    if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):        # ":=" is called walrus operator -- and -- with parentheses (...) a capturing group is created which we later used or captured in matches.group(), -- with (?:...) a group is created but it's non-capturing version of group is created
        print(f"Username: {matches.group(1)}")
    else:
        print("Not valid URL!")


twitter()