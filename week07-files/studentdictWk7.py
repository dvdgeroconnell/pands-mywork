# Program to implement part 5 of lab 07 (save the students)
# Author: David O'Connell  

import json

# use this file to save the students
FILENAME = "students.json"

# Function to print a menu of commands
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q): ").strip()
    return choice
    
def doAdd(students):
    print("in Add")
    new_student = {}
    new_student["name"] = input("New student name: ")
    print("Student:", new_student["name"])
    new_student["modules"] = readModules()
    students.append(new_student)

def doView(students):
    for student in students:
        print("Name:", student["name"])
        displayModules(student["modules"])

def doSave(students):
    with open(FILENAME, 'wt') as f:
        json.dump(students,f)
    with open(FILENAME, 'rt') as f:
        print(json.load(f))

def doLoad():
    with open(FILENAME, 'rt') as f:
        saved_students = json.load(f)
        print(saved_students)
    return saved_students

def displayModules(modules):
    for module in modules:
        print("Course:",module["name"])
        print("Grade:",module["grade"])

def readModules():

    # modules will be an array of dicts, each dict is a course name and grade
    modules = []

    module_name = 'a'
    while(module_name != ''):
        module = {} # build one dict per loop
        module_name = input("Enter the course name: ")
        if module_name != '':
            module_grade = int(input("Enter the grade: "))
            module["name"] = module_name
            module["grade"] = module_grade

            modules.append(module)

    for module in modules:
        print("\t", module["name"], "\t:",module["grade"])

    return modules # return the list of dicts, each dict is a course and grade

# main program

students = []

choice = ""
while (choice) !="q":
    choice = displayMenu()
    print("you chose",choice)
    if choice == "a":
        doAdd(students)
    elif choice =="v":
        doView(students)
    elif choice =="s":
        doSave(students)
    elif choice =="l":
        students = doLoad()