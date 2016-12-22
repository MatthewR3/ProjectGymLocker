# --------------------------------------------------
# Module Name:		StudentCount
# Purpose:			Counts the students belonging to a teacher
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
def main(teacher):

	# Calls database initialization function
	db, cursor = initialize()

	# Counts students belong to teacher
	cursor.execute("""SELECT COUNT(*) FROM gym_locker.students WHERE teacher = "%s" """ % (teacher))

	# Retrieves data
	value = cursor.fetchone()[0]

	# Closes database connection
	db.close()

	return value



# Direct Testing
if __name__ == "__main__":

	'''
	teacher = raw_input("Teacher: ")
	'''

	teacher = "Teivans"

	print main(teacher)
