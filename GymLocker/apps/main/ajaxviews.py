from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from GymLocker import services



def url_error(request):

	"FUNC AJAX URL ERROR"

	return HttpResponse("ERROR: INCORRECT AJAX URL")



def class_list(request, teacher, current_value):

	"FUNC AJAX CLASS LIST"

	user = teacher

	class_list = services.search_students("teacher", user)

	new_class_list = []

	if current_value == None:
		new_class_list = class_list
	else:
		for listing in class_list:
			try:
				if int(listing[8]) == int(current_value):
					new_class_list.append(listing)
			except:
				pass

	if current_value == None:
		current_value = ""

	return render(request, "ajaxclassview.html", {"class_list": new_class_list, "current_value": current_value})



def add_tardy(request, student_id):
	
	print "FUNC AJAX ADD TARDY"

	new_value = services.add_tardy(student_id)

	return HttpResponse(new_value)



def add_rental(request, student_id):
	
	print "FUNC AJAX ADD RENTAL"

	new_value = services.add_rental(student_id)

	return HttpResponse(new_value)



def search_students(request, limit):

	print "FUNC AJAX SEARCH STUDENTS"

	search_parameters = request.GET.getlist("search_parameters[]")
	search_values = request.GET.getlist("search_values[]")

	results = services.advanced_student_search(search_parameters, search_values, int(limit))

	return render(request, "ajaxsearchstudents.html", {"results": results})



def search_locks(request, limit):

	print "FUNC AJAX SEARCH LOCKS"

	search_parameters = request.GET.getlist("search_parameters[]")
	search_values = request.GET.getlist("search_values[]")

	results = services.advanced_lock_search(search_parameters, search_values, int(limit))

	results_list = []

	# Swaps values from tuple (MySQLdb default) to list
	for result in results:
		result_list = []
		for value in result:
			result_list.append(value)
		results_list.append(result_list)

	for result in results_list:
		if result[3] != None:
			student = services.search_student("student_id", result[3][:6])
			result[3] = student[3] + " " + student[2]
			result.append(student[0])

	return render(request, "ajaxsearchlocks.html", {"results": results_list})



def get_student(request, student_id):

	print "FUNC AJAX GET STUDENT"

	student = services.search_student("student_id", student_id)

	if student == None:
		return HttpResponse("ERROR: STUDENT NOT FOUND")

	owned_locks = False
	if student_id != "":
		owned_locks = services.search_locks("student id", int(student_id))

	return render(request, "ajaxindividualstudentview.html", {"student": student, "owned_locks": owned_locks})



def update_student(request, student_id, parameter, value):

	print "FUNC AJAX UPDATE STUDENT"

	new_value = services.update_student(student_id, parameter, value)

	if new_value == None:
		return HttpResponse("ERROR")

	return HttpResponse(new_value)



def get_lock(request, serial):

	print "FUNC AJAX GET LOCK"

	try:
		lock = services.search_lock("serial", serial)
		student_name = services.get_student_name(lock[3][:6])
		return render(request, "ajaxindividuallockview.html", {"lock": lock, "student_name": student_name})
	except:
		pass

	if lock == None:
		return HttpResponse("ERROR: LOCK NOT FOUND")

	return render(request, "ajaxindividuallockview.html", {"lock": lock})



def update_lock(request, serial, parameter, value):

	print "FUNC AJAX UPDATE LOCK"

	new_value = services.update_lock(serial, parameter, value)

	print "New Value: " + str(new_value)

	if new_value == None:
		return HttpResponse("ERROR")

	if parameter == "student_id":
		new_value = services.get_student_name(new_value[:6])

	print new_value
	return HttpResponse(new_value)