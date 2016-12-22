# --------------------------------------------------
# Module Name:		UpdateStudent
# Purpose:			Updates a student's attributes
# Author:			Matthew Rastovac
# Date Created:		4/24/15
#
# Current Version: 	1.0
# Last Modified:	6/01/15
# Last Change:		Returns "ERROR" instead of False for failed lookups
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(student_id, update_field, new_value):
	
	# Calls database initialization function
	db, cursor = initialize()

	try:
		student_key = get_student(student_id)
	except:
		print "Error: Cannot find student with given student_id. Exiting..."
		return "ERROR"

	# Changes update_field to correct database field names
	if update_field.upper() == "STUDENT ID" or update_field.upper() == "STUDENTID":
		update_field = 'student_id'
	elif update_field.upper() == "LAST NAME" or update_field.upper() == "LASTNAME":
		update_field = 'last_name'
	elif update_field.upper() == "FIRST NAME" or update_field.upper() == "FIRSTNAME":
		update_field = 'first_name'
	elif update_field.upper() == "LOCKER NUMBER" or update_field.upper() == "LOCKERNUMBER":
		update_field = 'locker_number'
	# Ensures that update_field is not surrounded by quotes and is lowercase so that query will run
	else:
		update_field = update_field.lower().strip('"\'')

	print update_field
	print new_value

	# Attempts to update student
	cursor.execute("""UPDATE gym_locker.students SET %s = "%s" WHERE student_key = "%s" """ % (update_field, new_value, student_key))

	# Commits changes to database
	db.commit()

	# Closes database connection
	db.close()

	return new_value



# Finds the student_key of a student with a given student_id
def get_student(student_id):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT student_key FROM gym_locker.students WHERE student_id = %d""" % (int(student_id)))
	student_key = cursor.fetchone()[0]

	return student_key



# Direct Testing
if __name__ == "__main__":

	'''
	student_id = raw_input("Student's ID Number: ")
	print "Options: Student ID, First Name, Last Name, YIS, Teacher, Period, Gender, Locker Number"
	update_field = raw_input("Update Field: ")
	new_value = raw_input("New Value: ")
	'''

	student_id = 150735
	update_field = "first name"
	new_value = "Matthew"

	print main(student_id, update_field, new_value)