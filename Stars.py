#Stars

#Write the following functions

#Part 1
#Create a function called draw_stars() that takes a list of numbers and prints out *.

x = [4,6,1,3,5,7,25]

def draw_stars(given_list):
    for idx in range(len(given_list)):
        print "*" * given_list[idx]

draw_stars(x)

"""
Part 2
Modify the function above. Allow a list containing integers and strings to be passed
to the draw_stars() function. When a string is passed, instead of displaying *,
display the first letter of the string according to the example below.
You may use the .lower() string method for this part.
"""

x2 = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_stars_part2(given_list):
    for idx in range(len(given_list)):
        if type(given_list[idx]) is int:
            print "*" * given_list[idx]
        elif type(given_list[idx]) is str:
            print given_list[idx][0] * len(given_list[idx])


draw_stars_part2(x2)
