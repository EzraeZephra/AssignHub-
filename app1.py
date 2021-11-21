import databaseS
from Student import*
 
MENU_PROMPT = """ - - student app - -
please choose one of these options:
 
1) add a new student
2) see all students
3) find a student by name
4) see the students in the course
5) clear table
6) exit
 
Your selection:
"""
 
nameD = ""
coursesName = ""
secondCourse = ""
thirdCourse = ""
 
def menu():
    global nameD,coursesName,secondCourse,thirdCourse
    connection = databaseS.connect()
    databaseS.create_tables(connection)
 
    while(user_input := input(MENU_PROMPT))!=6:
        if user_input =="1":
            nameD = input("Enter student name: ")
            coursesName = input("The first course that the student has: ")
            grade = input("Enter grade for student: ")
 
            databaseS.add_student(connection, nameD,coursesName,grade)
        elif user_input=="2":
            studentL = databaseS.getAllStudents(connection)
 
            for student in studentL:
                print(student)
        elif user_input=="3":
            name = input("Enter the name of the student that you're looking for")
            students = databaseS.getStudentByName(connection, name)
 
            for student in students:
                print(student)
        elif user_input=="4":
            course = input("Enter the course you're looking for")
            theStudentInCourse = databaseS.getStudentByCourse(connection, course)
 
            for student in theStudentInCourse:
                print(student)
        elif user_input=="5":
            databaseS.clear_everything(connection)
 
menu()
 
 
