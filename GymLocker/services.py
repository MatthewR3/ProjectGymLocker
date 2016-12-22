# --------------------------------------------------
# Module Name:		services
# Purpose:			Connects website data handling functions to business logic in external directories
# Author:			Matthew Rastovac
# Date Created:		5/21/15
#
# Current Version: 	1.0
# Last Modified:	1/14/16
# Last Change:		Edited advanced_student_search() function to support multiple search parameters
# --------------------------------------------------

# Note: Assuming Utilities folder's layout has not been modified, this should be the 
# only value in this module needing to be changed if project is reorganized
import Utilities

def student_count(teacher):

	import Utilities.DatabaseScripts.Other.StudentCount as student_count

	value = student_count.main(teacher)

	return value

def add_student(**kwargs):

	import Utilities.DatabaseScripts.Add.AddStudent as add

	status = add.main(**kwargs)

	return status

def add_lock(serial, combination, **kwargs):

	import Utilities.DatabaseScripts.Add.AddLock as add

	status = add.main(serial, combination, **kwargs)

	return status

def search_student(parameter, value):

	import Utilities.DatabaseScripts.Search.SearchStudent as search

	result = search.main(parameter, value)

	return result

def search_students(parameter, value):

	import Utilities.DatabaseScripts.Search.SearchStudents as search

	results = search.main(parameter, value)

	return results

def add_tardy(student_id):

	import Utilities.DatabaseScripts.Other.AddTardy as add

	new_value = add.main(student_id)

	return new_value

def add_rental(student_id):

	import Utilities.DatabaseScripts.Other.AddRental as add

	new_value = add.main(student_id)

	return new_value

def advanced_student_search(parameters, values, limit):

	import Utilities.DatabaseScripts.Search.AdvancedSearchStudents as search

	results = search.main(parameters, values, limit)

	return results

def advanced_lock_search(parameters, values, limit):

	import Utilities.DatabaseScripts.Search.AdvancedSearchLocks as search

	results = search.main(parameters, values, limit)

	return results

def update_student(student_id, parameter, value):

	import Utilities.DatabaseScripts.Update.UpdateStudent as update

	new_value = update.main(student_id, parameter, value)

	return new_value

def search_lock(parameter, value):

	import Utilities.DatabaseScripts.Search.SearchLock as search

	result = search.main(parameter, value)

	return result

def search_locks(parameter, value):

	import Utilities.DatabaseScripts.Search.SearchLocks as search

	results = search.main(parameter, value)

	return results

def update_lock(serial, parameter, value):

	import Utilities.DatabaseScripts.Update.UpdateLock as update

	new_value = update.main(serial, parameter, value)

	return new_value

def get_student_name(student_id):

	import Utilities.DatabaseScripts.Other.GetStudentName as get

	student_name = get.main(student_id)

	return student_name

def get_teacher_names():

	import Utilities.DatabaseScripts.Other.GetTeacherNames as get

	teacher_names = get.main()

	return teacher_names

def mass_student_edit(subset_attribute, subset_value, update_attribute, update_value):

	import Utilities.DatabaseScripts.Other.MassStudentEdit as edit

	status, reverse_query = edit.main(subset_attribute, subset_value, update_attribute, update_value)

	return status, reverse_query

def get_latest_query_record():

	import Utilities.DatabaseScripts.Other.GetLatestQueryRecord as get

	latest_query_record = get.main()

	return latest_query_record

def deconstruct_query(query):

	import Utilities.DatabaseScripts.Other.MassStudentEdit as edit

	subset_attribute, subset_value, update_attribute, update_value = edit.query_deconstructor(query)

	return subset_attribute, subset_value, update_attribute, update_value

def mass_student_delete(subset_attribute, subset_value):

	import Utilities.DatabaseScripts.Other.MassStudentDelete as delete

	status = delete.main(subset_attribute, subset_value)

	return status