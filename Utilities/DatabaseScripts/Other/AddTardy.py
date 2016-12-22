# --------------------------------------------------
# Module Name:		AddTardy
# Purpose:			Adds a tardy to a specified student
# Author:			Matthew Rastovac
# Date Created:		5/21/15
#
# Current Version: 	1.0
# Last Modified:	5/21/15
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
		return False

	# Associates lock with student
	cursor.execute("""UPDATE gym_locker.students SET tardies = tardies + 1 WHERE student_key = "%s" """ % (student_key))

	# Commits changes to database
	db.commit()

	# Retrieves new tardies value
	cursor.execute("""SELECT tardies FROM gym_locker.students WHERE student_key = "%s" """ % (student_key))
	new_value = cursor.fetchone()[0]

	# Closes database connection
	db.close()

	return new_value



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
