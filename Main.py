from Teacher import*

damienHighSchool = School()

noah = Student("noah","chemistry","calculus","language")
damienHighSchool.addStudent(noah)

damienHighSchool.addStudent(Student("sam", "chemistry", "calculus", "language"))
damienHighSchool.addStudent(Student("ivan", "statistics", "calculus", "literature"))
damienHighSchool.addStudent(Student("antong", "history", "calculus", "language"))
damienHighSchool.addStudent(Student("bob", "chemistry", "history", "statistics"))

edwards = Teacher("language",damienHighSchool)
chillingworth = Teacher("calculus",damienHighSchool)
dimmesdale = Teacher("chemistry",damienHighSchool)
winthrop = Teacher("history", damienHighSchool)
hibbins = Teacher("statistics", damienHighSchool)

chillingworth.addAssignment("KA Skills", 90)
dimmesdale.addAssignment("Ideal Gases Lab", 120)
winthrop.addAssignment("Civil War Essay", 80)

print("Noah's workload: " + str(noah.schoolwork))
print("Noah's workload time: " + str(noah.getTotalAssignmentTime()) + " minutes")
print("Avg Student Workload for language: " + str(edwards.getAverageStudentWorkload()) + " minutes.")
edwards.addAssignment("Frederick Douglass Essay", 120)

print("Noah's workload: " + str(noah.schoolwork))
print("Noah's workload time: " + str(noah.getTotalAssignmentTime()) + " minutes")
