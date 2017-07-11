#Dictionary Basics
#Making and Reading from Dictionaries
"""
Create a dictionary containing some information about yourself. The keys should
include name, age, country of birth, favorite language.

Write a function that will print something like the following as it executes:
My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python
"""

myself = {"Name": "Kishan", "Age": 99, "Birthplace": "Canada", "Favorite_language": "Python"}

def print_info(info):
    print "My name is",info["Name"]
    print "My age is",info["Age"]
    print "My country of birth is",info["Birthplace"]
    print "My favorite language is",info["Favorite_language"]

print_info(myself)
