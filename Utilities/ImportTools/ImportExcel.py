# --------------------------------------------------
# Module Name:		ImportExcel
# Purpose:			Imports locks from an excel sheet into database
# Author:			Matthew Rastovac
# Date Created:		8/1/15
#
# Current Version: 	1.0
# Last Modified:	8/1/15
# Last Change:		Began development
# --------------------------------------------------

import MySQLdb
import openpyxl

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from DatabaseScripts.Add import AddLock



def main(filename):

	path = "/var/www/gymlocker.com/Programming/ProjectGymLocker/Development/Utilities/ImportTools/Files/"

	with open(path + "locks.xlsx", "r") as f:

		lines = f.readlines()

		lock_dict = {}
		owner_dict = {}
		
		for line in lines:

			try:
				int(line[0])
			except:
				print "SKIPPING LINE: " + line
				continue

			lock = line.strip("\n").split(",")
			lock_dict[lock[0]] = lock[1]

			if lock[2] != "":
				owner_dict[lock[0]] = lock[2]

	for serial, combination in lock_dict.iteritems():

		if serial in owner_dict:
			AddLock.main(serial, combination, owned_by_student=True, student_id=owner_dict[serial])
			continue

		AddLock.main(serial, combination)





if __name__ == "__main__":

	main("locks.xlsx")