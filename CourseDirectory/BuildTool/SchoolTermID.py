class SchoolTerm(object):
	
	year = ""
	termID = 0
	termName = ""
	termLength = 0
	
	def newTerm(self):	
		self.setTermYear()
		self.setTermID()
		self.setTermLength()

	def setTermID(self):
		
		# Declare private variables
		termIDStr = ""
		
		while(len(termIDStr) != 1):
			
			# Present the desired term ids
			print("0 = Fall term")
			print("1 = Spring term")
			print("2 = Summer term")
			print("===============")
			
			# Prompt for the term ID
			termIDStr = input("Enter term ID: ")
			print("")
			
			# Validate that the entered ID is between 0 and 2 and is numeric
			if(termIDStr.isnumeric()):
				if(not (abs(int(termIDStr,10)) <= 2)):
					termIDStr = ""
				else:
					self.termID = abs(int(termIDStr,10))
					self.setTermName()
			else:
				termIDStr = ""

	def setTermYear(self):
		
		# Force the input to be a 4 character year code
		while(len(self.year) != 4):
			self.year = input("What year is it?")
			
			if(not self.year.isnumeric()):
				self.year = ""
			
			
	def setTermName(self):
		
		# Set the term name per the term ID
		if(self.termID == 2):
			self.termName = "Summer"
		elif(self.termID == 1):
			self.termName = "Spring"
		else:
			self.termName = "Fall"
	
	def setTermLength(self):
		while(not ((self.termLength == 8) or (self.termLength == 16))):
			length = input("How long is the term? [8] or [16] weeks: ")
			if(length.isnumeric):
				self.termLength = int(length,10)
	
	def toString(self) -> str:
		# Return the contents of the object in a single string
		return(self.year + "--0" + str(self.termID) + "_" + self.termName)