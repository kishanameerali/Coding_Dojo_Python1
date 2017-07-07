#Scores and Grades

"""
Write a function that generates ten scores between 60 and 100. Each time a score is
generated, your function should display what the grade is for a particular score.
Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
"""

import random

def class_grades():
    for result in range(10):
        mark = random.randint(60,101)
        if mark < 70:
            grade = "D"
            print "Score: " + str(mark) + "; Your grade is",grade
        elif mark < 80 and mark > 69:
            grade = "C"
            print "Score: " + str(mark) + "; Your grade is",grade
        elif mark < 90 and mark > 79:
            grade = "B"
            print "Score: " + str(mark) + "; Your grade is",grade
        else:
            grade = "A"
            print "Score: " + str(mark) + "; Your grade is",grade
    print "End of the program. Bye!"

class_grades()
