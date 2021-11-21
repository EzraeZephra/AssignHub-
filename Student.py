class Student:
    name = ""

    def __init__(self, name: str, course1: str, course2: str, course3: str):
        self.schoolwork = {}
        self.name = name
        self.schoolwork[course1] = {}
        self.schoolwork[course2] = {}
        self.schoolwork[course3] = {}

    def getSchoolwork(self):
        return self.schoolwork

    def addAssignment(self, course: str, assignmentName: str, assignmentTime: int):
        self.schoolwork[course][assignmentName] = assignmentTime

    def removeAssignment(self, course: str, assignmentName: str):
        self.schoolwork[course].pop(assignmentName)

    def getTotalAssignmentTime(self):
        totalTime = 0
        for key,value in self.schoolwork.items():
            for k,v in self.schoolwork[key].items():
                totalTime += v
        return totalTime

    """def printWorkload(self):
        for key,value in self.schoolwork.items():
            for k,v in self.schoolwork[key].items():"""










