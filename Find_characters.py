#Find Characters

#Write a program that takes a list of strings and a string containing a single character,
#and prints a new list of all the strings containing that character.

word_list = ["hello","world","my","name","is","Anna"]
char = "m"
new_list = []

for idx in range (0,len(word_list)):
    if word_list[idx].count(char) > 0:
        new_list.append(word_list[idx])

print "word_list =",word_list
print "char =",char
print "new_list =",new_list
