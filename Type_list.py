#Type List

"""
Write a program that takes a list and prints a message for each element in the list,
based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type.
If the item is a string, concatenate it onto a new string.
If it is a number, add it to a running sum. At the end of your program print the string,
the number and an analysis of what the array contains. If it contains only one type,
print that type, otherwise, print 'mixed'.
"""

a = [2,5,8,-65,0,-3,45]
b = ["horses","chickens","rabbits"]
ab = ["horses",5,-17,"cows",67.43,"birds",-3.4]
l = ['magical unicorns',19,'hello',98.98,'world']
sum = 0
new_string = ""

example = l
array = ""

for i in range(0,len(example)):
    if all(isinstance(example,int) for example in example): #if all(isinstance(x, SubclassOne) for x in list_of_stuff):
        array = "int"
    elif all(isinstance(example,str) for example in example):
        array = "str"
    else:
        array = "mixed"

for idx in range(0,len(example)):
    if type(example[idx]) is int or type(example[idx]) is float:
        sum = sum + example[idx]
    elif type(example[idx]) is str:
        new_string = new_string +" " + example[idx]


if array == "int":
    print "The array you entered is of integer type"
    print "Sum:",sum
elif array == "str":
    print "The array you entered is of string type"
    print "String:",new_string
elif array == "mixed":
    print "The array you entered is of mixed type"
    print "String:",new_string
    print "Sum:",sum
