# --------------------------------------------------
# Module Name:		AdvancedSearchStudents
# Purpose:			Searches for multiple students with more operability, including comparison operators and wildcard matching
# Author:			Matthew Rastovac
# Date Created:		5/22/15
#
# Current Version: 	1.1
# Last Modified:	1/14/16
# Last Change:		Modified to allow multiple search parameters
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(search_parameters, search_values, limit):

	query_base = """SELECT * FROM gym_locker.students WHERE"""

	first = True;
	for search_parameter, search_value in zip(search_parameters, search_values):

		# Changes search_parameter to correct database field names
		if search_parameter.upper() == "STUDENT ID":
			search_parameter = 'student_id'
		elif search_parameter.upper() == "LAST NAME":
			search_parameter = 'last_name'
		elif search_parameter.upper() == "FIRST NAME":
			search_parameter = 'first_name'
		elif search_parameter.upper() == "LOCKER NUMBER":
			search_parameter = 'locker_number'
		# Ensures that search_parameter is not surrounded by quotes and is lowercase so that query will run
		else:
			search_parameter = search_parameter.lower().strip('"\'')

		# Returns all records if the value entered is ONLY an operator
		if search_value == ">" or search_value == "<":
			search_value = ">0"

		# Enforces lowercase values for search_parameter and search_value
		try:
			search_parameter = search_parameter.lower()
			search_value = search_value.lower()
		except:
			pass

		# Checks if parameter allows comparison operators and calls input parser function if so
		operator_parameters = ["student_id", "yis", "period", "tardies", "rentals"]
		if search_parameter in operator_parameters:
			partial_query = input_parser(search_parameter, search_value)
		else:
			partial_query = like_query_constructor(search_parameter, search_value)

		if first:
			query_base += """ """ + partial_query;
			first = False;
		else:
			query_base += """ AND """ + partial_query;

	query = query_base + """ LIMIT %d""" % (limit)

	# Calls database initialization function
	db, cursor = initialize()

	# Performs database search
	cursor.execute(query)

	# Gathers results
	search_results = cursor.fetchall()

	# Closes database connection
	db.close()

	return search_results



# Parses input to remove any comparison operators and calls query constructor
def input_parser(search_parameter, search_value):

	# If operator is found in string, separates string into operator and value substrings, then passes data to query constructor
	if ">" in search_value or "<" in search_value:
		operator = search_value[0]
		search_value = int(search_value[1:])
		query = operator_query_constructor(search_parameter, search_value, operator)
	else:
		query = like_query_constructor(search_parameter, search_value)

	return query


# Constructs custom SQL query based on parsed input with an operator
def operator_query_constructor(search_parameter, search_value, operator):

	operator_query = """%s %s %s""" % (search_parameter, operator, search_value)

	return operator_query



# Constructs custom SQL query based on parsed input without an operator
def like_query_constructor(search_parameter, search_value):

	# Appends the "%" SQL wildcard (matches zero or more characters) to search_value
	try:
		search_value += "%"
	except:
		search_value = "%"

	like_query = """%s LIKE "%s" """ % (search_parameter, search_value)

	return like_query



# Direct Testing
if __name__ == "__main__":

	'''
	print "Options: Student ID, First Name, Last Name, YIS, Teacher, Period, Gender, Locker Number"
	search_parameter = raw_input("Search Parameter: ")
	search_value = raw_input("Search Value: ")
	'''

	search_parameter = "yis"
	search_value = ">2"

	results = main(search_parameter, search_value)

	if results == ():
		print "Empty"
	else:
		for result in results:
			print result