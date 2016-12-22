# --------------------------------------------------
# Module Name:		DeleteLock
# Purpose:			Deletes a lock
# Author:			Matthew Rastovac
# Date Created:		4/24/15
#
# Current Version: 	1.0
# Last Modified:	5/18/15
# Last Change:		Changed incorrect database initialization
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

	# Deletes user from database
	cursor.execute("""DELETE FROM gym_locker.locks WHERE lock_key = "%s" """ % (lock_key))

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

	serial = 123456789

	main(serial)