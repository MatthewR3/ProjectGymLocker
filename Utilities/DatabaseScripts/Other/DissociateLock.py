# --------------------------------------------------
# Module Name:		DissociateLock
# Purpose:			Deletes the association between a student and a lock
# Author:			Matthew Rastovac
# Date Created:		4/26/15
#
# Current Version: 	1.0
# Last Modified:	4/27/15
# Last Change:		Began development
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(serial):

	# Calls database initialization function
	db, cursor = initialize()

	try:
		lock_key = get_lock(serial)
	except:
		print "Error: Cannot find lock with given serial. Exiting..."
		return False

	# Dissociates lock from student
	cursor.execute("""UPDATE gym_locker.locks SET student_key = "" WHERE lock_key = "%s" """ % (lock_key))

	# Commits changes to database
	db.commit()

	# Closes database connection
	db.close()

	return True



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
	serial = raw_input("Serial Number: ")
	'''

	serial = 123456788

	main(serial)