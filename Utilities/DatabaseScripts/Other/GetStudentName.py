# --------------------------------------------------
# Module Name:		GetStudentName
# Purpose:			Retrieves the full name of a student given a student_id
# Author:			Matthew Rastovac
# Date Created:		6/01/15
#
# Current Version: 	1.0
# Last Modified:	6/01/15
# Last Change:		Began development
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(student_id):

	# Calls database initialization function
	db, cursor = initialize()

	try:
		student_key = get_student(student_id)
	except:
		print "Error: Cannot find student with given ID. Exiting..."
		return "STUDENT NOT FOUND"

	# Retrisves first and last name of student
	cursor.execute("""SELECT first_name, last_name FROM gym_locker.students WHERE student_key = "%s" """ % (student_key))

	# Retrieves values and concatenates into a full name
	name_list = cursor.fetchall()[0]
	student_name = name_list[0] + " " + name_list[1]

	# Closes database connection
	db.close()

	return student_name



# Finds the student_key of a student with a given id
def get_student(student_id):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT student_key FROM gym_locker.students WHERE student_id = "%s" """ % (student_id))
	student_key = cursor.fetchone()[0]

	return student_key



# Direct Testing
if __name__ == "__main__":

	'''
	student_id = raw_input("Student ID: ")
	'''

	student_id = 150735

	print main(student_id)
