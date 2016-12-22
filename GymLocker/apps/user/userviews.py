from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from GymLocker.apps.user.forms import LoginForm



def login_user(request):

	print "FUNC LOGIN"
	
	if request.method == 'POST':

		form = LoginForm(request.POST)

		if form.is_valid():

			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					print "Logged in " + str(user)
					return HttpResponseRedirect("/")
				else:
					# Return a 'disabled account' error message
					return HttpResponse("Account Disabled: See Technology Support Intern")
			else:
				return HttpResponse("Invalid Login. Try again.")
		else:
			print "Form not valid"

	login_form = LoginForm()

	return render(request, "login.html", {'login_form': login_form})



@login_required
def logout_user(request):

	"FUNC LOGOUT"
	
	logout(request)

	print "Logged out " + str(request.user) + ", now redirecting to login"

	return HttpResponseRedirect("/user/login/")