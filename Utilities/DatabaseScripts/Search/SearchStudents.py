# --------------------------------------------------
# Module Name:		SearchStudents
# Purpose:			Searches for multiple students
# Author:			Matthew Rastovac
# Date Created:		5/20/15
#
# Current Version: 	1.0
# Last Modified:	5/20/15
# Last Change:		Began Development
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(search_parameter, search_value):

	# Calls database initialization function
	db, cursor = initialize()

	# Changes search_parameter to correct database field names
	if search_parameter.upper() == "STUDENT ID":
		search_parameter = 'student_id'
	elif search_parameter.upper() == "LAST NAME":
		search_parameter = 'last_name'
	elif search_parameter.upper() == "FIRST NAME":
		search_parameter = 'first_name'
	elif search_parameter.upper() == "LOCKER NUMBER":
		search_parameter = 'locker_number'
	# Ensures that search_parameter is not surrounded by quotes and is lowercase so that query will run
	else:
		search_parameter = search_parameter.lower().strip('"\'')

	# Performs database search
	cursor.execute("""SELECT * FROM gym_locker.students WHERE %s = "%s" """ % (search_parameter, search_value))

	# Gathers results
	search_results = cursor.fetchall()

	# Closes database connection
	db.close()

	return search_results



# Direct Testing
if __name__ == "__main__":

	'''
	print "Options: Student ID, First Name, Last Name, YIS, Teacher, Period, Gender, Locker Number"
	search_parameter = raw_input("Search Parameter: ")
	search_value = raw_input("Search Value: ")
	'''

	search_parameter = "period"
	search_value = "7"

	print main(search_parameter, search_value)