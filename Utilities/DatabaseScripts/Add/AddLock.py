# --------------------------------------------------
# Module Name:		AddLock
# Purpose:			Adds a lock to a user
# Author:			Matthew Rastovac
# Date Created:		4/24/15
#
# Current Version: 	1.0
# Last Modified:	5/20/15
# Last Change:		Changed "raw_input" to "input" in testing to return boolean instead of string (causing failed tests)
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(serial, combination, owned_by_student=False, student_id=None):

	# Attempts to generate unique lock key, and exits if an error is thrown
	try:	
		lock_key = gen_key(serial, combination)
	except:
		print "Error: Cannot generate unique key. Exiting..."
		return False

	# Calls database initialization function
	db, cursor = initialize()

	# Calls function to check for originality of lock
	if not is_original(serial, combination):
		print "Duplicate lock found"
		return "unoriginal"

	# Adds a lock with an association to a student
	if owned_by_student == True:

		try:
			student_key = get_student(student_id)
		except:
			print "Error: Cannot find student with given student_id. Exiting..."
			return "missing"

		# Inserts lock into database with given parameters
		cursor.execute("""INSERT INTO 
							gym_locker.locks(lock_key, serial, combination, student_key) 
							VALUES("%s", "%s", "%s", "%s")""" 
							% (lock_key, serial, combination, student_key))

	else:

		# Inserts lock into database with given parameters
		cursor.execute("""INSERT INTO 
							gym_locker.locks(lock_key, serial, combination) 
							VALUES("%s", "%s", "%s")""" 
							% (lock_key, serial, combination))
	
	# Commits changes to database
	db.commit()

	# Closes database connection
	db.close()

	return True



# Generates unique key for student (enforces data uniqueness in case two students have the same ID number)
def gen_key(serial, combination):
	
	key = str(str(serial) + str(combination))[:20]

	return key



# Finds the student_key of a student with a given student_id
def get_student(student_id):

	print student_id
	print type(student_id)

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT student_key FROM gym_locker.students WHERE student_id = %d""" % (int(student_id)))
	student_key = cursor.fetchone()[0]

	print student_key

	return student_key



# Checks if the lock already exists
def is_original(serial, combination):

	# Calls database initialization function
	db, cursor = initialize()

	cursor.execute("""SELECT * FROM gym_locker.locks WHERE serial = "%s" AND combination = "%s" """ % (serial, combination))
	locks = cursor.fetchall()

	if locks == ():
		return True

	return False



# Direct Testing
if __name__ == "__main__":

	
	serial = raw_input("Serial Number: ")
	combination = raw_input("Combination: ")
	owned_by_student = input("Is lock owned by a student (True/False): ")
	if owned_by_student == True:
		student_id = int(raw_input("Student's ID Number: "))
		main(serial, combination, owned_by_student=True, student_id=student_id)
	else:
		main(serial, combination)
	'''

	serial = 123456789
	combination = "11-11-11"
	owned_by_student = True
	student_id = 150735
	'''