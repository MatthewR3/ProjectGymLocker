from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from GymLocker import services

from GymLocker.apps.main.forms import AddStudentForm, AddLockForm



@login_required
def homepage(request):

	print "FUNC HOMEPAGE"

	student_count = services.student_count(request.user)

	return render(request, "homepage.html", {"user": request.user, "student_count": student_count})



@login_required
def class_view(request, user):

	print "FUNC CLASS VIEW"

	student_count = services.student_count(request.user)

	class_list = services.search_students("teacher", user)

	return render(request, "classview.html", {"user": request.user, "student_count": student_count, "class_list": class_list})



@login_required
def search_students(request):

	print "FUNC SEARCH STUDENTS"

	student_count = services.student_count(request.user)

	return render(request, "searchstudents.html", {"user": request.user, "student_count": student_count})



@login_required
def search_locks(request):

	print "FUNC SEARCH LOCKS"

	student_count = services.student_count(request.user)

	return render(request, "searchlocks.html", {"user": request.user, "student_count": student_count})



@login_required
def individual_student_view(request, student_id):

	print "FUNC INDIVIDUAL STUDENT VIEW"

	student_count = services.student_count(request.user)

	student = services.search_student("student_id", student_id)

	owned_locks = False
	if student_id != "":
		owned_locks = services.search_locks("student id", int(student_id))

	return render(request, "individualstudentview.html", {"user": request.user, "student_count": student_count, "student": student, "owned_locks": owned_locks})



@login_required
def individual_lock_view(request, serial=""):

	print "FUNC INDIVIDUAL LOCK VIEW"

	student_count = services.student_count(request.user)

	try:
		lock = services.search_lock("serial", serial)
		student_name = services.get_student_name(lock[3][:6])
		return render(request, "individuallockview.html", {"user": request.user, "student_count": student_count, "lock": lock, "student_name": student_name})
	except:
		pass

	return render(request, "individuallockview.html", {"user": request.user, "student_count": student_count, "lock": lock})



@login_required
def add_student(request, serial=""):

	print "FUNC ADD STUDENT"

	form = AddStudentForm()

	student_count = services.student_count(request.user)


	if request.method == "POST":

		form = AddStudentForm(request.POST)

		if form.is_valid():

			student_id = form.cleaned_data["student_id"]
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			yis = form.cleaned_data["yis"]
			teacher = form.cleaned_data["teacher"]
			period = form.cleaned_data["period"]
			gender = form.cleaned_data["gender"]
			locker_number = form.cleaned_data["locker_number"]
			note = form.cleaned_data["note"]

			status = services.add_student(student_id=student_id, first_name=first_name, last_name=last_name, yis=yis, teacher=teacher, period=period, gender=gender, locker_number=locker_number, note=note)

			if status == False or status == "unoriginal":
				return render(request, "addstudentdone.html", {"user": request.user, "student_count": student_count, "status": status})
			else:
				student = services.search_student("student_id", student_id)
				return render(request, "addstudentdone.html", {"user": request.user, "student_count": student_count, "status": status, "student": student})

	return render(request, "addstudent.html", {"user": request.user, "student_count": student_count, "form": form})



@login_required
def add_lock(request, serial=""):

	print "FUNC ADD LOCK"

	form = AddLockForm()

	student_count = services.student_count(request.user)

	form = AddLockForm(request.POST)

	if request.method == "POST":

		if form.is_valid():

			serial = form.cleaned_data["serial"]
			combination = form.cleaned_data["combination"]
			owner = form.cleaned_data["owner"]

			if owner == "":
				status = services.add_lock(serial, combination)
			else:
				status = services.add_lock(serial, combination, owned_by_student=True, student_id=owner)

			if status == False or status == "missing":
				return render(request, "addlockdone.html", {"user": request.user, "student_count": student_count, "status": status})
			else:
				lock = services.search_lock("serial", serial)
				owner = services.search_student("student_key", lock[3])
				return render(request, "addlockdone.html", {"user": request.user, "student_count": student_count, "status": status, "lock": lock, "owner": owner})


	return render(request, "addlock.html", {"user": request.user, "student_count": student_count, "form": form})



@login_required
def class_view_prompt(request):

	print "FUNC CLASS VIEW PROMPT"

	student_count = services.student_count(request.user)

	teacher_names = services.get_teacher_names()

	return render(request, "classviewprompt.html", {"user": request.user, "student_count": student_count, "teacher_names": teacher_names})



@login_required
def mass_student_edit(request):

	print "FUNC MASS STUDENT EDIT"

	student_count = services.student_count(request.user)

	return render(request, "massstudentedit.html", {"user": request.user, "student_count": student_count})



@login_required
def mass_student_edit_confirmation(request, subset_attribute, subset_value, update_attribute, update_value):

	print "FUNC MASS STUDENT EDIT CONFIRMATION"

	student_count = services.student_count(request.user)

	return render(request, "massstudenteditconfirmation.html", {"user": request.user, "student_count": student_count, "subset_attribute": subset_attribute, "subset_value": subset_value, "update_attribute": update_attribute, "update_value": update_value})



@login_required
def mass_student_edit_confirmed(request, subset_attribute, subset_value, update_attribute, update_value):

	print "FUNC MASS STUDENT EDIT CONFIRMED"

	student_count = services.student_count(request.user)

	status, reverse_query = services.mass_student_edit(subset_attribute, subset_value, update_attribute, update_value)

	return render(request, "massstudenteditconfirmed.html", {"user": request.user, "student_count": student_count, "subset_attribute": subset_attribute, "subset_value": subset_value, "update_attribute": update_attribute, "update_value": update_value, "status": status})



@login_required
def mass_student_edit_reverse_confirmation(request):

	print "FUNC MASS STUDENT EDIT REVERSE CONFIRMATION"

	student_count = services.student_count(request.user)

	latest_query_record = services.get_latest_query_record()
	reverse_query = latest_query_record[2]

	try:

		subset_attribute, subset_value, update_attribute, update_value = services.deconstruct_query(reverse_query)

		return render(request, "massstudenteditreverseconfirmation.html", {"user": request.user, "student_count": student_count, "reverse_query": reverse_query, "subset_attribute": subset_attribute, "subset_value": subset_value, "update_attribute": update_attribute, "update_value": update_value})	
	
	except:

		return render(request, "massstudenteditreverseconfirmation.html", {"user": request.user, "student_count": student_count, "reverse_query": reverse_query})



@login_required
def mass_student_delete(request):

	print "FUNC MASS STUDENT DELETE"

	student_count = services.student_count(request.user)

	return render(request, "massstudentdelete.html", {"user": request.user, "student_count": student_count})



@login_required
def mass_student_delete_confirmation(request, subset_attribute, subset_value):

	print "FUNC MASS STUDENT DELETE CONFIRMATION"

	student_count = services.student_count(request.user)

	return render(request, "massstudentdeleteconfirmation.html", {"user": request.user, "student_count": student_count, "subset_attribute": subset_attribute, "subset_value": subset_value})



@login_required
def mass_student_delete_confirmed(request, subset_attribute, subset_value):

	print "FUNC MASS STUDENT DELETE CONFIRMED"

	student_count = services.student_count(request.user)

	status = services.mass_student_delete(subset_attribute, subset_value)

	return render(request, "massstudentdeleteconfirmed.html", {"user": request.user, "student_count": student_count, "subset_attribute": subset_attribute, "subset_value": subset_value, "status": status})