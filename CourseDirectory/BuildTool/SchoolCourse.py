import os

class SchoolCourse(object):
	
	# Course ID MUST be 5 characters
	courseID = "#"
	# Course family ID must be between 3 and 4 characters
	courseFamily = "#"
	# Course number MUST be 4 characters (numbers or letters)
	courseNum = "#"
	# Course name
	courseName = "#"
	# Course professor
	courseProfessor = "#"
	
	def __init__(self):
		self.setCourseID()
		self.setCourseFamily()
		self.setCourseNum()
		self.setCourseInfo()
	
	def setCourseID(self):
		while((not self.courseID.isnumeric()) or (not (len(self.courseID) == 5))):
			self.courseID = input("Enter course ID: ")
	
	def setCourseFamily(self):
		while((not self.courseFamily.isalpha()) or (not ((len(self.courseFamily) >=3) and (len(self.courseFamily) <=4)))):
			self.courseFamily = input("Enter course family/category: ").upper()
	
	def setCourseNum(self):
		while((not (len(self.courseNum) == 4)) and (not self.courseNum.isalnum())):
			self.courseNum = input("Enter the course number: ").upper()
		
	def setCourseInfo(self):
		while(not self.courseName.isalnum()):
			self.courseName = input("Enter the course name in CamelCase4Info \n Letters and Numbers only (NoSpaces) \n Course Name: ")
		while(not self.courseProfessor.isalpha()):
			self.courseProfessor = input("Enter the professors name: ")
	
	def courseDirectory(self) -> str:
		return(self.courseID + "--" + self.courseFamily + "-" + self.courseNum)
	
	def courseInfo(self) -> str:
		return(self.courseName + "--Professor_" +self.courseProfessor+".info") 