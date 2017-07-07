#Multiples Part 1 - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for num in range(1,1000):
    if num%2 !=0:
        print num

#Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000

for mul in range(5,1000000):
    if mul%5 ==0:
        print mul

#Sum List - Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1,2,5,10,255,3]
print a
print "The sum of a is", sum(a)

#Average List - Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

print "The average of a is", sum(a)/len(a)

#Alternative Solution

#multiples A
#for count in range(1, 1001, 2):
    #print count

#multiples B
#for count in range(5,1000001,5):
    #print count

#sum list
#my_numbers = [1, 2, 5, 10, 255, 3]
#sum = 0
#for i in my_numbers:
    #sum += i
#print sum

#average list
#print sum/len(my_numbers)
