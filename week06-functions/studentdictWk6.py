# Program to implement parts 4 and 5 of weekly lab 05
# Author: David O'Connell  

# Function to print a menu of commands
def displayMenu():
    print("What would you like to do?")
    print("(a) Add new student")
    print("(v) View students")
    print("(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice
    
def doAdd(students):
    print("in Add")
    new_student = {}
    new_student["name"] = input("New student name: ")
    print("Student:", new_student["name"])
    new_student["modules"] = readModules()
    students.append(new_student)
    return

def doView(students):
    
    for student in students:
        print("Name:", student["name"])
        displayModules(student["modules"])

    return

def displayModules(modules):

    for module in modules:
        print("Course:",module["name"])
        print("Grade:",module["grade"])

    return

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



'''

student = {
    "name" : "Mary",
    "courses" : [
        {
            "coursename":"Programming",
            "grade":45
        },
        {
            "coursename":"History",
            "grade":99
        }
    ]
}

students.append(student)

#print("student",student)
#print("students",students)

print("Student:", student["name"])

for course in student["courses"]:
    print("\t", course["coursename"], "\t:",course["grade"])

new_course = 'a'
while(new_course != ''):
    new_course = input("Enter the next course name: ")
    if new_course != '':
        new_grade = input("Enter the grade: ")
        student["courses"].append({"coursename":new_course, "grade":new_grade})

print("Student:", student["name"])

for course in student["courses"]:
    print("\t", course["coursename"], "\t:",course["grade"])

    '''