# --------------------------------------------------
# Module Name:		DeleteStudent
# Purpose:			Deletes a student
# Author:			Matthew Rastovac
# Date Created:		4/24/15
#
# Current Version: 	1.0
# Last Modified:	4/26/15
# Last Change:		Changed incorrect database initialization
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(student_id):

	db, cursor = initialize()

	try:
		student_key = get_student(student_id)
	except:
		print "Error: Cannot find student with given student_id. Exiting..."
		return False

	# Deletes any locks owned by student
	cursor.execute("""DELETE FROM gym_locker.locks WHERE student_key = "%s" """ % (student_key))

	# Deletes user from database
	cursor.execute("""DELETE FROM gym_locker.students WHERE student_key = "%s" """ % (student_key))

	# Commits changes to database
	db.commit()

	# Closes database connection
	db.close()

	return True



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
	student_id = raw_input("Student's ID Number: ")
	'''

	student_id = 150737

	main(student_id)