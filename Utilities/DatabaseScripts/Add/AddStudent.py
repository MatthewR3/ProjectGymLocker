# --------------------------------------------------
# Module Name:		AddStudent
# Purpose:			Adds a student
# Author:			Matthew Rastovac
# Date Created:		4/24/15
#
# Current Version: 	1.0
# Last Modified:	6/9/15
# Last Change:		Added kwarg parsing and changed period to be compatible with database changing field from INT(11) to VARCHAR(2)
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(**kwargs):

	student_id = int(kwargs.get("student_id", ""))
	first_name = str(kwargs.get("first_name", ""))
	last_name = str(kwargs.get("last_name", ""))
	yis = int(kwargs.get("yis", ""))
	teacher = str(kwargs.get("teacher", ""))
	period = str(kwargs.get("period", ""))
	gender = str(kwargs.get("gender", ""))
	locker_number = str(kwargs.get("locker_number", ""))
	note = str(kwargs.get("note", ""))

	# Attempts to generate unique student key, and exits if an error is thrown
	try:	
		student_key = gen_key(student_id, yis, last_name)
	except:
		print "Error: Cannot generate unique key. Exiting..."
		return False

	# Calls database initialization function
	db, cursor = initialize()

	# Calls function to check for originality of student
	if not is_original(student_id):
		print "Duplicate student found"
		return "unoriginal"

	# Inserts user into database with given parameters
	cursor.execute("""INSERT INTO 
						gym_locker.students(student_key, student_id, last_name, first_name, yis, teacher, period, gender, locker_number, note) 
						VALUES("%s", %d, "%s", "%s", %d, "%s", "%s", "%s", "%s", "%s")""" 
						% (student_key, student_id, last_name, first_name, yis, teacher, period, gender, locker_number, note))
	
	# Commits changes to database
	db.commit()

	# Closes database connection
	db.close()

	return True



# Generates unique key for student (enforces data uniqueness in case two students have the same ID number)
def gen_key(student_id, last_name, yis):
	
	key = str(str(student_id) + str(yis) + str(last_name))[:20]

	return key



# Checks if the student already exists
def is_original(student_id):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT * FROM gym_locker.students WHERE student_id = "%s" """ % (student_id))
	students = cursor.fetchall()

	if students == ():
		return True

	return False



# Direct Testing
if __name__ == "__main__":

	'''
	student_id = int(raw_input("Student's ID Number: "))
	first_name = raw_input("Student's First Name: ")
	last_name = raw_input("Student's Last Name: ")
	yis = int(raw_input("YIS: "))
	teacher = raw_input("Teacher: ")
	period = int(raw_input("Period: "))
	gender = raw_input("Gender: ")
	locker_number = raw_input("Locker Number: ")
	note = raw_input("Note: ")
	'''

	student_id = 150751
	first_name = "12345678901234567890"
	last_name = "12345678901234567890"
	yis = 2015
	teacher = "Intern"
	period = 4
	gender = "Male"
	locker_number = "123-5"
	note="Random Note"
	
	main(student_id=student_id, first_name=first_name, last_name=last_name, yis=yis, teacher=teacher, period=period, gender=gender, locker_number=locker_number, note=note)
