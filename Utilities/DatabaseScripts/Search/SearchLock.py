# --------------------------------------------------
# Module Name:		SearchLock
# Purpose:			Searches for a lock
# Author:			Matthew Rastovac
# Date Created:		4/24/15
#
# Current Version: 	1.0
# Last Modified:	5/18/15
# Last Change:		Changed incorrect database initialization
# --------------------------------------------------

# Note: This version only retrieves one lock per query. If there are multiple locks with the same search_value
# for its search_parameter, the function will only return one of the locks.

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(search_parameter, search_value):

	# Calls database initialization function
	db, cursor = initialize()

	# Searches for a lock with a specific student_id
	if search_parameter.upper() == "STUDENT ID":

		try:
			student_key = get_student(search_value)
			search_parameter = "student_key"
			search_value = student_key
		except:
			print "Error: Cannot find student with given student_id. Exiting..."
			return False

	# Performs database search
	cursor.execute("""SELECT * FROM gym_locker.locks WHERE %s = "%s" """ % (search_parameter, search_value))

	# Gathers results
	search_results = cursor.fetchone()

	# Closes database connection
	db.close()

	return search_results



# Finds the student_key of a student with a given student_id
def get_student(student_id):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT student_key FROM gym_locker.students WHERE student_id = %d""" % (student_id))
	student_key = cursor.fetchone()[0]

	return student_key



# Direct Testing
if __name__ == "__main__":

	'''
	search_parameter = raw_input("Search Parameter (Serial/Combination/Student ID): ")
	search_value = raw_input("Search Value: ")
	'''

	search_parameter = "serial"
	search_value = 123456789

	print main(search_parameter, search_value)