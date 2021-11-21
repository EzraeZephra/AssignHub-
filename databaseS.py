import sqlite3
 
CREATE_STUDENTS_TABLE = "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER);"
 
INSERT_STUDNET = "INSERT INTO students (name, course, grade) VALUES (?, ?, ?);"
 
get_all_students = "SELECT * FROM students;"
 
clear_everything = "DELETE * FROM students;"
 
get_student_by_name = "SELECT * FROM students WHERE name = ?;"
 
get_student_in_course = """
SELECT * FROM students
Where name = ?
ORDER BY course
 
"""
 
def connect():
    return sqlite3.connect("dataC.db")
 
def create_tables(connection):
    with connection:
        connection.execute(CREATE_STUDENTS_TABLE)
 
def add_student(connection, name, course, grade):
    with connection:
        connection.execute(INSERT_STUDNET, (name, course, grade))
 
def getAllStudents(connection):
    with connection:
        return connection.execute(get_all_students).fetchall()
 
def getStudentByName(connection,name):
    with connection:
        return connection.execute(get_student_by_name,(name, )).fetchall()
 
def getStudentByCourse(connection, course):
    with connection:
        return connection.execute(get_student_in_course, (course,)).fetchall()
def clearAll(connection):
    with connection:
        connection.execute(clear_everything)
