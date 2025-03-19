
def studList():
	studentNames =['Lisa','Liam','Leo','Larry','Linda']
	for studentName in studentNames:
		print(studentName + " Evans")
	return studentNames

def addToList(studentList):
	name = input("please enter the name you want to add:")
	studentList.append(name)
	for studentName in studentList:
		print(studentName + "Evans")
	
s1 = studList()
addToList(s1)
