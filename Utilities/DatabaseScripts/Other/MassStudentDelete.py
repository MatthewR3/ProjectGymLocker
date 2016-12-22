# --------------------------------------------------
# Module Name:		MassStudentDelete
# Purpose:			Deletes multiple students with a common value
# Author:			Matthew Rastovac
# Date Created:		6/02/15
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
def main(subset_attribute, subset_value):

	# Assigns the default query type
	query_type = "normal"

	# Changes inputs to proper format
	if subset_attribute.upper() == "ID":
		subset_attribute = "student_id"
	if subset_attribute.upper() == "FIRST NAME":
		subset_attribute = "first_name"
	if subset_attribute.upper() == "LAST NAME":
		subset_attribute = "last_name"
	if subset_attribute.upper() == "LOCKER NUMBER":
		subset_attribute = "locker_number"

	# Assigns a different query type if the subset value is "all"; this will make query_constructor() omit the WHERE clause
	if subset_value.upper() == "ALL" or subset_value.upper() == "*":
		query_type = "all"

	# Retrieves comparison operator if one is used, and value of comparison
	if ">" in subset_value or "<" in subset_value:
		operator = subset_value[0]
		subset_value = subset_value[1:]
	else:
		operator = "="

	# Calls database initialization function
	db, cursor = initialize()

	try:

		# Passes attributes and values to query constructor
		#query = query_constructor(query_type, operator, subset_attribute, subset_value)
		query = query_constructor(query_type, operator, subset_attribute, subset_value)

		# Executes query
		cursor.execute(query)

		# Commits changes to database
		db.commit()

		status = "successful"

		print "QUERY: " + query

		# Inserts query record into database with given parameters
		cursor.execute("""INSERT INTO gym_locker.query_records(query) VALUES('%s')""" % (query))

		# Commits changes to database
		db.commit()

	except:

		status = "failure"

		# Reverts changes to database
		db.rollback()

	# Closes database connection
	db.close()

	return status



# Constructs query to update student attributes
def query_constructor(query_type, operator, subset_attribute, subset_value):

	# Constructs DELETE clause
	query = """DELETE FROM gym_locker.students"""

	# Adds WHERE clause
	if query_type == "normal":
		query += """ WHERE %s %s "%s" """ % (subset_attribute, operator, subset_value)

	return query



# Deconstructs a query into subset_attribute, subset_value
def query_deconstructor(query):

	print "DECONSTRUCTING QUERY: " + query

	subset_attribute = "Unassigned"
	subset_value = "Unassigned"

	# Determines subset_attribute and subset_value
	if "WHERE" not in query:
		subset_attribute = "student_id"
		subset_value = "all"
	else:
		space_count = 0
		subset_value = ""
		subset_attribute = ""
		for index, character in reversed(list(enumerate(query))):
			#print character
			if character == " ":
				space_count += 1
			if space_count == 0:
				first_space_index = index
				subset_value += character
			if space_count == 2:
				subset_attribute += character
		subset_attribute = subset_attribute.strip(" ")
		subset_value = subset_value.strip(" ")
		subset_value = subset_value.strip("\"")
		subset_attribute = subset_attribute[::-1]
		subset_value = subset_value[::-1]

		if ">" in query:
			subset_value = ">" + subset_value
		elif "<" in query:
			subset_value = "<" + subset_value
	


	# Changes inputs to proper format
	if subset_attribute.upper() == "STUDENT_ID":
		subset_attribute = "ID"
	if subset_attribute.upper() == "FIRST_NAME":
		subset_attribute = "First Name"
	if subset_attribute.upper() == "LAST_NAME":
		subset_attribute = "Last Name"
	if subset_attribute.upper() == "LOCKER_NUMBER":
		subset_attribute = "Locker Number"

	print "VALUES"
	print subset_attribute
	print subset_value

	return subset_attribute, subset_value





# Direct Testing
if __name__ == "__main__":

	'''
	subset_attribute = raw_input("Subset Attribute: ")
	subset_value = raw_input("Subset Value: ")
	update_attribute = raw_input("Update Attribute: ")
	update_value = raw_input("Update Value: ")
	'''

	subset_attribute = "yis"
	subset_value = "<2016"

	'''
	DELETE students WHERE yis = 2015
	DELETE students WHERE yis > 2015
	DELETE students WHERE yis < 2015
	'''

	#print main(subset_attribute, subset_value)
	print query_deconstructor("""DELETE students WHERE yis < 2015""")
