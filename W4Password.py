# Write a Python program to check the validity of a password (input from users)
#
# Rules :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z]
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# If password is not valid throw ValueError with a proper error message for each rule. If the password is valid print a success message. Use some from raise, except, assert, else and finally keywords.
import re
password=input("Please enter a password")
match=re.match(r'[A-Za-z](\w|$|#|@)+',password)
print(match)

