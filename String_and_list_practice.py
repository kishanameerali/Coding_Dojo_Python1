#Strings and List Practice
"""
In this string: words = "It's thanksgiving day. It's my birthday,too!"
print the position of the first instance of the word "day".
Then create a new string where the word "day" is replaced with the word "month".
"""

words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
new_string = words.replace("day","month")
print new_string

#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98].
#Your code should work for any list.

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

"""
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
Now create a new list containing only the first and last values in the original list.
Your code should work for any list.
"""

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]
new_list = [y[0],y[len(y)-1]]

"""
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first.
Then, split your list in half. Push the list created from the first half to position 0 of the
list created from the second half.
The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
"""

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
z_first_half = z[:len(z)/2]
z_second_half = z[len(z)/2:]
z_second_half = [z_first_half] + z_second_half
print z_second_half


#x = [19,2,54,-2,7,12,98,32,10,-3,6]
#print x
#x.sort()
#print x
#first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
#second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
#print "first list", first_list
#print "second_list", second_list
#second_list.insert(0,first_list)
#print second_list
