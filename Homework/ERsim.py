#  File: ERsim.py
#  Description: Use a queue to treat patients at a hospital
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 03/04/2017
#  Date Last Modified: 03/04/2017


#----------------------- Classes -----------------------#


class Queue:
	'''
	FIFO queue abstract data type implemented using lists
	'''
	
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		self.items.insert(0,item)
		
	def dequeue(self):
		return self.items.pop()
		
	def size(self):
		return len(self.items)
	
	def peek(self):
		return self.items[-1]
	
	def __str__(self):
		return str(self.items)


#----------------------- Functions -----------------------#


def readFile(fileName, critQ, serQ, fairQ):
	'''
	Read in the file and process each line using helper functions
	'''
	
	inFile = open(fileName, "r")
	
	# go through all the lines and apply the correct function
	for line in inFile:
		line = line.split()
		# the action is always the first word
		action = line[0]
		
		# adding a patient
		if(action == "add"):
			# line[1]: patient name, line[2]: patient condition
			handleAdd(line[1], line[2], critQ, serQ, fairQ)
			
		# treating a patient
		elif(action == "treat"):
			# line[1]: condition type
			handleTreat(line[1], critQ, serQ, fairQ)
			
		# exiting the program
		elif(action == "exit"):
			exit()
			return
	
	infile.close()
	return


def handleAdd(patient, condition, critQ, serQ, fairQ):
	'''
	add patient to the appropriate queue
	'''
	
	print()
	print("Add patient %s to %s queue" % (patient, condition))
	# handle which queue the patient is added to
	if(condition == "Critical"):
		critQ.enqueue(patient)
	elif(condition == "Serious"):
		serQ.enqueue(patient)
	elif(condition == "Fair"):
		fairQ.enqueue(patient)
		
	print()
	queuesState(critQ, serQ, fairQ)


def handleTreat(condition, critQ, serQ, fairQ):
	'''
	treat the next patient, based on the criteria if there is one
	'''

	# general treat next case
	if(condition == "next"):
		print()
		print("Treat next patient")
		print()
		
		# check critical queue first
		if (not critQ.isEmpty()):
			patient = critQ.dequeue()
			print("Treating '%s' from Critical queue" % (patient))
			queuesState(critQ, serQ, fairQ)
			
		# check serious queue next
		elif (not serQ.isEmpty()):
			patient = serQ.dequeue()
			print("Treating '%s' from Serious queue" % (patient))
			queuesState(critQ, serQ, fairQ)
			
		# check fair queue last
		elif (not fairQ.isEmpty()):
			patient = fairQ.dequeue()
			print("Treating '%s' from Fair queue" % (patient))
			queuesState(critQ, serQ, fairQ)
			
		# if all queues are empty, tell the user
		else:
			print("No patients in queues")
			
	# if told to treat all patients
	elif(condition == "all"):
		print()
		print("Treat all patients")
		
		# treat all critical patients
		while(not critQ.isEmpty()):
			print()
			patient = critQ.dequeue()
			print("Treating '%s' from Critical queue" % (patient))
			queuesState(critQ, serQ, fairQ)
			
		# treat all serious patients
		while(not serQ.isEmpty()):
			print()
			patient = serQ.dequeue()
			print("Treating '%s' from Serious queue" % (patient))
			queuesState(critQ, serQ, fairQ)
			
		# treat all fair patients
		while(not fairQ.isEmpty()):
			print()
			patient = fairQ.dequeue()
			print("Treating '%s' from Fair queue" % (patient))
			queuesState(critQ, serQ, fairQ)
			
		# print that there are no patients left
		print()
		print("No patients in queues")
	
	# if given a specific type to treat
	else:
		print()
		print("Treat next patient on %s queue" % (condition))
		print()
		
		# if treating critical queue
		if (condition == "Critical"):
			# treat next patient in critical queue
			if(not critQ.isEmpty()):
				patient = critQ.dequeue()
				print("Treating '%s' from Critical queue" % (patient))
				queuesState(critQ, serQ, fairQ)
			# if no patients, tell the user
			else:
				print("No patients in queue")
			
		# if treating serious queue
		elif (condition == "Serious"):
			# treat next patient in serious queue
			if(not serQ.isEmpty()):
				patient = serQ.dequeue()
				print("Treating '%s' from Serious queue" % (patient))
				queuesState(critQ, serQ, fairQ)
			# if no patients, tell the user
			else:
				print("No patients in queue")
			
		# if treating fair queue
		elif (condition == "Fair"):
			# treat next patient in fair queue
			if(not fairQ.isEmpty()):
				patient = fairQ.dequeue()
				print("Treating '%s' from Fair queue" % (patient))
				queuesState(critQ, serQ, fairQ)
			# if no patients, tell the user
			else:
				print("No patients in queue")
	 

def exit():
	'''
	Exit and quit the program
	'''
	
	print()
	print("Exit")
	print()
	return


def queuesState(critQ, serQ, fairQ):
	'''
	print all of the queues
	'''
	print("Queues are:")
	print("Critical: %s" % (critQ))
	print("Serious:  %s" % (serQ))
	print("Fair:     %s" % (fairQ))

	
#----------------------- Main Function -----------------------#


def main():
	
	# name of file
	fileName = "ERsim.txt"
	# initialize the three queues for the three types of patients
	critQ = Queue()
	serQ = Queue()
	fairQ = Queue()
	
	# function that runs through all the lines of the file and prints what happens
	readFile("ERsim.txt", critQ, serQ, fairQ)
	
if __name__ == "__main__":
	main()
	