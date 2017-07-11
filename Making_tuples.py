#Making Tuples
#Dictionary in, tuples out
"""
Write a function that takes in a dictionary and returns a list of tuples where
the first tuple item is the key and the second is the value.
"""

my_dict = {
    "Alvin": "(111)111-1111",
    "Simon": "(222)222-2222",
    "Theodore": "(333)333-3333"
}

new_list = []

def tuple_list(chipmunks):
    return chipmunks.items()

print tuple_list(my_dict)
