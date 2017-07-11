#Names

#Given the following list:

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

#Create a program that outputs:
"""
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
"""

def names(name_list):
    for idx in range(len(name_list)):
        print name_list[idx]['first_name'],name_list[idx]['last_name']

names(students)

#Part 2

#Now, given the following dictionary:

users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

"""
Create a program that prints the following format
(including number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
"""

def user_records(records):
    for key,data in records.items():
        print key
        position = 0
        for value in data:
            position = position + 1
            print position,"-",value['first_name'],value['last_name'],"-",len(value['first_name'] + value['last_name'])

user_records(users)
