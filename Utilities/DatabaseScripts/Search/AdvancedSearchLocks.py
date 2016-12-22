# --------------------------------------------------
# Module Name:		AdvancedSearchLocks
# Purpose:			Searches for multiple locks with more operability, including wildcard matching
# Author:			Matthew Rastovac
# Date Created:		5/22/15
#
# Current Version: 	1.0
# Last Modified:	5/22/15
# Last Change:		Began Development
# --------------------------------------------------

import MySQLdb

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from InitializeDatabase import initialize



# Main module function
def main(search_parameters, search_values, limit):

	query_base = """SELECT * FROM gym_locker.locks WHERE"""

	first = True;
	for search_parameter, search_value in zip(search_parameters, search_values):

		# Enforces lowercase values for search_parameter and search_value
		try:
			search_parameter = search_parameter.lower()
			search_value = search_value.lower()
		except:
			pass

		partial_query = query_constructor(search_parameter, search_value)

		if first:
			query_base += """ """ + partial_query;
			first = False;
		else:
			query_base += """ AND """ + partial_query;

	query = query_base + """ LIMIT %d""" % (limit)

	# Calls database initialization function
	db, cursor = initialize()

	# Performs database search
	print query
	cursor.execute(query)

	# Gathers results
	search_results = cursor.fetchall()

	# Closes database connection
	db.close()

	return search_results



# Constructs custom SQL query based on parsed input without an operator
def query_constructor(search_parameter, search_value):

	# Appends the "%" SQL wildcard (matches zero or more characters) to search_value
	try:
		search_value += "%"
	except:
		search_value = "%"

	query = """%s LIKE "%s" """ % (search_parameter, search_value)

	return query



# Direct Testing
if __name__ == "__main__":

	'''
	print "Options: Serial, Combination"
	search_parameter = raw_input("Search Parameter: ")
	search_value = raw_input("Search Value: ")
	'''

	search_parameter = "serial"
	search_value = "2"

	results = main(search_parameter, search_value)

	if results == ():
		print "Empty"
	else:
		for result in results:
			print result