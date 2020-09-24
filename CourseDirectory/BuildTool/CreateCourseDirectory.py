import os
from SchoolTermID import SchoolTerm
from SchoolCourse import SchoolCourse

currentTerm = SchoolTerm()
currentTerm.newTerm()
print("=================")
print("Current term info")
print("=================")
print(currentTerm.toString())

continueAdding = ""
while(continueAdding == ""):
	# Create a new course object
	course = SchoolCourse()
	
	# Validate course info
	print("Adding course info: " + course.courseInfo() + "\ninto directory\n" + course.courseDirectory())
	
	# Build path
	coursePath ="D:/" + currentTerm.toString() + "/" + course.courseDirectory() 
	os.makedirs(coursePath,exist_ok=True)
	
	# Create info file
	courseInfoFile = open(coursePath + "/" + course.courseInfo(),"w")
	courseInfoFile.close()
	
	# Build content management
	week = 1
	os.makedirs(coursePath + "/LongProjects",exist_ok=True)
	while(week <= currentTerm.termLength):
	
		# Local level week string
		weekStr = ""
		
		# Validate string length
		if(len(str(week)) < 2):
			weekStr = "0" + str(week)
		else:
			weekStr = str(week)
		# Make the directory and increment
		os.makedirs(coursePath + "/ContentManagement/Week" + weekStr + "/SubmissionPile",exist_ok=True)
		os.makedirs(coursePath + "/ContentManagement/Week" + weekStr + "/ReadingPile",exist_ok=True)
		os.makedirs(coursePath + "/ContentManagement/Week" + weekStr + "/ReferenceMateral",exist_ok=True)
		week += 1
	
	continueAdding = input("Continue adding courses? []")
	

