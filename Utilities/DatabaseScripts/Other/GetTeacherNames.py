# --------------------------------------------------
# Module Name:		GetTeacherNames
# Purpose:			Retrieves all possible teacher names based on unique values in the database
# Author:			Matthew Rastovac
# Date Created:		6/01/15
#
# Current Version: 	1.0
# Last Modified:	6/01/15
# Last Change:		Began development
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main():

	# Calls database initialization function
	db, cursor = initialize()

	# Retrieves unique values of teacher names
	cursor.execute("""SELECT DISTINCT(teacher) FROM gym_locker.students""")

	# Retrieves values
	teacher_names = cursor.fetchall()

	# Formats retrieves values into django form required syntax
	teacher_names_tuple = (("", "Select Teacher"),)
	for teacher in teacher_names:
		if teacher[0] == "":
			pass
		else:
			teacher += (teacher[0],)
			teacher_names_tuple += (teacher,)

	# Closes database connection
	db.close()

	return teacher_names_tuple



# Direct Testing
if __name__ == "__main__":

	print main()
