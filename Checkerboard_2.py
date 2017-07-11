#Checkerboard Assignment using nested for loops

#Write a program that prints a 'checkerboard' pattern to the console.


for row in range(1,9):
    for col in range(1,9):
        if (row % 2 is odd and col % 2 is 0):
            print " "
        if (row % 2 is 0 and col % 2 is 0):
