# --------------------------------------------------
# Module Name:		UpdateLock
# Purpose:			Updates a lock's attributes
# Author:			Matthew Rastovac
# Date Created:		4/24/15
#
# Current Version: 	1.0
# Last Modified:	6/01/15
# Last Change:		Returns "" instead of False for failed student lookup
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(serial, update_field, new_value):

	print "RIGHT"
	
	# Calls database initialization function
	db, cursor = initialize()

	try:
		lock_key = get_lock(serial)
	except:
		print "Error: Cannot find lock with given serial. Exiting..."
		return "ERROR"

	if update_field.upper() == "STUDENT ID" or update_field.upper() == "STUDENT_ID":

		try:
			student_key = get_student(new_value)
			update_field = "student_key"
			new_value = student_key
		except:
			print "Error: Cannot find student with given student_id. Exiting..."
			return ""

	# Attempts to update student
	cursor.execute("""UPDATE gym_locker.locks SET %s = "%s" WHERE lock_key = "%s" """ % (update_field, new_value, lock_key))

	# Commits changes to database
	db.commit()

	# Closes database connection
	db.close()

	return new_value



# Finds the lock_key of a lock with a given serial
def get_lock(serial):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT lock_key FROM gym_locker.locks WHERE serial = "%s" """ % (serial))
	lock_key = cursor.fetchone()[0]

	return lock_key



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

	serial = 123456789
	update_field = "combination"
	new_value = "11-11-11"

	print main(serial, update_field, new_value)