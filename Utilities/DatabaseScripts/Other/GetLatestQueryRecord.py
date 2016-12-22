# --------------------------------------------------
# Module Name:		GetLatestQueryRecord
# Purpose:			Retrieves last performed query's record
# Author:			Matthew Rastovac
# Date Created:		6/03/15
#
# Current Version: 	1.0
# Last Modified:	6/03/15
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

	# Retrieves last performed query's record
	cursor.execute("""SELECT * FROM gym_locker.query_records ORDER BY record_number DESC LIMIT 1""")

	# Retrieves values
	record = cursor.fetchone()

	# Closes database connection
	db.close()

	return record



# Direct Testing
if __name__ == "__main__":

	print main()
