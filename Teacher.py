from School import*

class Teacher:

    course = ""
    school = ""

    def __init__(self, course: str, school: School):
        self.course = course
        self.school = school

    def addAssignment(self, assignmentName: str, assignmentTime: int):
        for student in self.school.students:
            if self.course in student.schoolwork:
                student.addAssignment(self.course,assignmentName,assignmentTime)

    def removeAssignment(self,assignmentName):
        for student in self.school.students:
            if self.course in student.schoolwork:
                student.removeAssignment(self.course,assignmentName)

    def getAverageStudentWorkload(self):
        totalTime = 0
        studentsInCourse = 0
        for student in self.school.students:
            if self.course in student.schoolwork:
                studentsInCourse += 1
                totalTime += student.getTotalAssignmentTime()
        return int(totalTime/studentsInCourse)

    def printStudentWorkload(self,studentName: str):
        for student in self.school.students:
            if student.name == studentName:
                print(student.schoolwork)
