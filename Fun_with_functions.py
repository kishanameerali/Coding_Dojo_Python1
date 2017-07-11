#Fun with Functions
"""
Create a function called odd_even that counts from 1 to 2000.
As your loop executes have your program print the number of that iteration and
specify whether it's an odd or even number.
"""

def odd_even():
    for count in range (1,2001):
        if count % 2 == 0:
            print "Number is" + str(count) + ".  This is an even number."
        else:
            print "Number is" + str(count) + ".  This is an odd number."

odd_even()

"""
Create a function called 'multiply' that iterates through each value in a list
(e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument.
"""

def multiply(arr,num):
    for idx in range (len(arr)):
        arr[idx] = arr[idx]*num
    return arr

a = [1,2,3,4]

#print multiply(a,2)

"""
Write a function that takes the multiply function call as an argument.
Your new function should return the multiplied list as a two-dimensional list.
Each internal list should contain the number of 1's as the number in the original list.
"""

def layered_multiples(arr):
    print arr
    two_dimension_list = []
    for idx in range (len(arr)):
        print arr[idx]
        inner_list = []
        for num in range(arr[idx]):
            inner_list.append(1)
        two_dimension_list.append(inner_list)
    print two_dimension_list

layered_multiples(multiply(a,2))
