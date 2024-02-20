students = {

    "Josh":[],
    "John":[],

}


def adding_grades(name):
    done = input("Do you want to add to their grades? y or n :")
    while done == "y":
     
        name.append(int(input("grade: ")))
        done = input("Do you want to continue? y or n :")


def new_student():
    new_name = input("what is the name of the student: ")
    students[new_name] = []
    adding_grades(students[new_name])


def find_average(student):
    average = 0


    for i in student:
        average += i 
      

    print("Score range:" , min(student), "-" ,max(student))
    print("Second check: " ,len(students))
    print(students)
    print("Avg: ", average/ len(students))


    return average


def check_grade():
    grades = input("Who's grade do you want check :")
    print("Grades: ",(students[grades]))
    adding_grades(students[grades])
    print("first check: ", len(students[grades]))
    find_average(students[grades])



add_student = input("Do you want to add a new student? y or n:")


if add_student == "y":
    new_student()
    check = input("Do you want to check someones grade y or n :")

    if check == "y":
        check_grade()

    else:
        pass
else:
    check_grade()







