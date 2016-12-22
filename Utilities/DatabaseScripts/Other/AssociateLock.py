# --------------------------------------------------
# Module Name:		AssociateLock
# Purpose:			Makes an association between a student and a lock
# Author:			Matthew Rastovac
# Date Created:		5/18/15
#
# Current Version: 	1.0
# Last Modified:	5/18/15
# Last Change:		Began development
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(student_id, serial):

	# Calls database initialization function
	db, cursor = initialize()

	try:
		student_key = get_student(student_id)
	except:
		print "Error: Cannot find student with given ID. Exiting..."
		return False

	try:
		lock_key = get_lock(serial)
	except:
		print "Error: Cannot find lock with given serial. Exiting..."
		return False

	# Associates lock with student
	cursor.execute("""UPDATE gym_locker.locks SET student_key = "%s" WHERE lock_key = "%s" """ % (student_key, lock_key))

	# Commits changes to database
	db.commit()

	# Closes database connection
	db.close()

	return True



# Finds the student_key of a student with a given id
def get_student(student_id):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT student_key FROM gym_locker.students WHERE student_id = "%s" """ % (student_id))
	student_key = cursor.fetchone()[0]

	return student_key



# Finds the lock_key of a lock with a given serial
def get_lock(serial):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT lock_key FROM gym_locker.locks WHERE serial = "%s" """ % (serial))
	lock_key = cursor.fetchone()[0]

	return lock_key



# Direct Testing
if __name__ == "__main__":

	'''
	student_id = raw_input("Student ID: ")
	serial = raw_input("Serial Number: ")
	'''

	student_id = 150735
	serial = 123456788

	main(student_id, serial)
