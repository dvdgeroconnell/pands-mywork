# Program to implement parts 4 and 5 of weekly lab 05
# Author: David O'Connell  

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

print(student)

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