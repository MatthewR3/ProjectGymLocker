# --------------------------------------------------
# Module Name:		MassStudentEdit
# Purpose:			Edits multiple students with a common value for a specific attribute
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
def main(subset_attribute, subset_value, update_attribute, update_value):

	# Assigns the default query type
	query_type = ("normal",)

	# Changes inputs to proper format
	if subset_attribute.upper() == "ID":
		subset_attribute = "student_id"
	if subset_attribute.upper() == "FIRST NAME":
		subset_attribute = "first_name"
	if subset_attribute.upper() == "LAST NAME":
		subset_attribute = "last_name"
	if subset_attribute.upper() == "LOCKER NUMBER":
		subset_attribute = "locker_number"
	
	if update_attribute.upper() == "FIRST NAME":
		update_attribute = "first_name"
	if update_attribute.upper() == "LAST NAME":
		update_attribute = "last_name"
	if update_attribute.upper() == "LOCKER NUMBER":
		update_attribute = "locker_number"

	# Assigns a different query type if the subset value is "all"; this will make query_constructor() omit the WHERE clause
	if subset_value.upper() == "ALL" or subset_value.upper() == "*":
		query_type = ("all",)

	# If operation is arithmetic, retrieves arithmetic operator and value, then constructs query-legal statement
	update_value_int = ""
	if "+" in update_value or "-" in update_value:
		arithmetic_operator = update_value[0]
		update_value_int = update_value[1:]
		update_value = update_attribute + " %s %s" % (arithmetic_operator, update_value_int)
		query_type += ("arithmetic",)

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
		query, reverse_query = query_constructor(query_type, operator, subset_attribute, subset_value, update_attribute, update_value, update_value_int)

		# Executes query
		cursor.execute(query)

		# Commits changes to database
		db.commit()

		status = "successful"

		print "QUERY: " + query
		print "REVERSE QUERY: " + reverse_query

		# Inserts query record into database with given parameters
		cursor.execute("""INSERT INTO gym_locker.query_records(query, reverse_query) VALUES('%s', '%s')""" % (query, reverse_query))

		# Commits changes to database
		db.commit()

	except:

		status = "failure"

		# Reverts changes to database
		db.rollback()

	# Closes database connection
	db.close()

	return status, reverse_query



# Constructs query to update student attributes
def query_constructor(query_type, operator, subset_attribute, subset_value, update_attribute, update_value, update_value_int):

	# Constructs UPDATE clause based on whether the update value is an arithmetic function or not
	if "arithmetic" in query_type:
		query = """UPDATE gym_locker.students SET %s = %s""" % (update_attribute, update_value)
	else:
		query = """UPDATE gym_locker.students SET %s = "%s" """ % (update_attribute, update_value)

	# Adds WHERE clause
	if "normal" in query_type:
		query += """ WHERE %s %s "%s" """ % (subset_attribute, operator, subset_value)

	reverse_query = reverse_query_constructor(query_type, operator, subset_attribute, subset_value, update_attribute, update_value, update_value_int, query)

	return query, reverse_query



# Constructs reverse query for queries where it is possible to revert changes
def reverse_query_constructor(query_type, operator, subset_attribute, subset_value, update_attribute, update_value, update_value_int, query):

	# Only arithmetic changes can be reverted
	if "arithmetic" in query_type:

		# Reverses arithmetic operator
		reverse_update_value = update_value.replace("+", "-")
		if update_value == reverse_update_value:
			reverse_update_value = update_value.replace("-", "+")

		# If subset_value cannot be converted to int, assigns that value to subset_value
		try:
			subset_value = int(subset_value)
			# Manipulates update_value_int to reflect post-query value
			if "+" in update_value:
				reverse_subset_value = int(subset_value) + int(update_value_int)
			elif "-" in update_value:
				reverse_subset_value = int(subset_value) - int(update_value_int)
		except:
			reverse_subset_value = subset_value

		# Constructs UPDATE clause based on whether the update value is an arithmetic function or not
		reverse_query = """UPDATE gym_locker.students SET %s = %s""" % (update_attribute, reverse_update_value)

		# Adds WHERE clause
		if "normal" in query_type:
			reverse_query += """ WHERE %s %s "%s" """ % (subset_attribute, operator, reverse_subset_value)

		return reverse_query

	else:

		return "impossible"



# Deconstructs a query into subset_attribute, subset_value, update_attribute, and update_value
def query_deconstructor(query):

	print "DECONSTRUCTING QUERY: " + query

	subset_attribute = "Unassigned"
	subset_value = "Unassigned"
	update_attribute = "Unassigned"
	update_value = "Unassigned"

	# Determines update_attribute
	equal_index = query.index("=")
	equal_index -= 1
	update_attribute = ""
	for character in reversed(query[:equal_index]):
		if character == " ":
			break;
		update_attribute += character
	update_attribute = update_attribute[::-1]

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
			if space_count == 1:
				first_space_index = index
				subset_value += character
			if space_count == 3:
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
	
	# Determines update_value
	if "+" in query or "-" in query:
		try:
			arithmetic_index = query.index("+")
		except:
			arithmetic_index = query.index("-")
		arithmetic_index += 2
		update_value = ""
		for character in query[arithmetic_index:]:
			if character == " ":
				break;
			update_value += character
		if "+" in query:
			update_value = "+" + update_value
		elif "-" in query:
			update_value = "-" + update_value
	else:
		equal_index += 3
		update_value = ""
		for character in query[equal_index:]:
			if character == " ":
				break;
			update_value += character
	update_value = update_value.strip("\"")

	# Changes inputs to proper format
	if subset_attribute.upper() == "STUDENT_ID":
		subset_attribute = "ID"
	if subset_attribute.upper() == "FIRST_NAME":
		subset_attribute = "First Name"
	if subset_attribute.upper() == "LAST_NAME":
		subset_attribute = "Last Name"
	if subset_attribute.upper() == "LOCKER_NUMBER":
		subset_attribute = "Locker Number"
	
	if update_attribute.upper() == "FIRST_NAME":
		update_attribute = "First Name"
	if update_attribute.upper() == "LAST_NAME":
		update_attribute = "Last Name"
	if update_attribute.upper() == "LOCKER_NUMBER":
		update_attribute = "Locker Number"

	print "VALUES"
	print subset_attribute
	print subset_value
	print update_attribute
	print update_value

	return subset_attribute, subset_value, update_attribute, update_value





# Direct Testing
if __name__ == "__main__":

	'''
	subset_attribute = raw_input("Subset Attribute: ")
	subset_value = raw_input("Subset Value: ")
	update_attribute = raw_input("Update Attribute: ")
	update_value = raw_input("Update Value: ")
	'''

	subset_attribute = "yis"
	subset_value = "*"
	update_attribute = "yis"
	update_value = "30"

	'''
	UPDATE students SET yis = yis + 30
	UPDATE students SET yis = yis + 30 WHERE yis = 2015
	UPDATE students SET yis = yis + 1 WHERE yis < 2015
	UPDATE students SET yis = yis - 1 WHERE period > 2015
	UPDATE students SET first_name = "Matthew" WHERE period < 4
	UPDATE students SET last_name = "Rastovac" WHERE period > 6
	'''

	print main(subset_attribute, subset_value, update_attribute, update_value)
	#print query_deconstructor("""UPDATE gym_locker.students SET YIS = YIS - 1 WHERE student_id > "1" """)
