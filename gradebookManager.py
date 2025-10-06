grades = {
    "Dave": [90, 85, 88],
    "Alice": [92, 81, 79],
    "Marsh": [12, 14, 11],
}


#Add a new student
def addStudent():
    global grades
    choice = input("What is the student's name?: ")
    grades[choice] = []
    print("Student added.")


#Delete student
def deleteStudent():
    global grades
    choice = input("What is the student's name?: ")
    if choice in grades:
        del grades[choice]
        print("Student deleted.")
    else:
        print("Student not found.")


#Add grades for existing student
def addGrades():
    global grades
    choice = input("What is the student's name?: ")
    if choice in grades:
        grade = int(input("Enter the grade to add: "))
        grades[choice].append(grade)
        print("Grade added.")
    else: print("Student not found.")


#Delete grades
def deleteGrades():
    global grades
    choice = input("What is the student's name?: ")
    if choice in grades:
        print("Current grades:", grades[choice])
        grade = int(input("Enter the grade to delete: "))
        if grade in grades[choice]:
            grades[choice].remove(grade)
            print("Grade deleted.")
        else:
            print("Grade not found.")
    else: print("Student not found.")


#View the gradebook summary
def viewGradebook():
    for student, student_grades in grades.items():
        print(student, student_grades)


#View averages
def viewAverages():
    global grades
    for student, student_grades in grades.items():
        if student_grades:
            average = sum(student_grades) / len(student_grades)
            print(student, "average:", round(average, 2))
        else:
            print(student, "has no grades.")


def options():
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Add Grades")
    print("4. Delete Grades")
    print("5. View Gradebook")
    print("6. View Averages")
    print("7. Exit")


def main():
    while True:
        print("/////////////////////////")
        options()
        choice = int(input("What would you like to do?: "))
        if choice == 1:
            addStudent()
        elif choice == 2:
            deleteStudent()
        elif choice == 3:
            addGrades()
        elif choice == 4:
            deleteGrades()
        elif choice == 5:
            viewGradebook()
        elif choice == 6:
            viewAverages()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

main()