from django.conf.urls import patterns, include, url

from GymLocker.apps.main import mainviews



urlpatterns = patterns('',
	url(r'^view/class/prompt/', mainviews.class_view_prompt),
	url(r'^view/class/([\Wa-zA-Z0-9]*)', mainviews.class_view),
	url(r'^view/individual/students/([0-9]*)', mainviews.individual_student_view),
	url(r'^view/individual/locks/([0-9]*)', mainviews.individual_lock_view),
	url(r'^search/students/', mainviews.search_students),
	url(r'^search/locks/', mainviews.search_locks),
	url(r'^add/students/', mainviews.add_student),
	url(r'^add/locks/', mainviews.add_lock),
	url(r'^edit/mass/confirm/([_a-zA-Z\s_]*)/([<>\*a-zA-Z0-9\s-]*)/([a-zA-Z\s]*)/([\+a-zA-Z0-9\s-]*)', mainviews.mass_student_edit_confirmation),
	url(r'^edit/mass/([_a-zA-Z\s]*)/([<>\*a-zA-Z0-9\s-]*)/([a-zA-Z\s]*)/([\+a-zA-Z0-9\s-]*)', mainviews.mass_student_edit_confirmed),
	url(r'^edit/mass/reverse/confirm/', mainviews.mass_student_edit_reverse_confirmation),
	url(r'^edit/mass/', mainviews.mass_student_edit),
	url(r'^delete/mass/confirm/([_a-zA-Z\s_]*)/([<>\*a-zA-Z0-9\s-]*)', mainviews.mass_student_delete_confirmation),
	url(r'^delete/mass/([_a-zA-Z\s_]*)/([<>\*a-zA-Z0-9\s-]*)', mainviews.mass_student_delete_confirmed),
	url(r'^delete/mass/', mainviews.mass_student_delete),
	url(r'^', mainviews.homepage),
)