from django.conf.urls import patterns, include, url

from GymLocker.apps.main import ajaxviews


urlpatterns = patterns('',
	url(r'^class_list/([a-zA-Z-]*)/(\d+)?', ajaxviews.class_list),
	url(r'^add_tardy/(\d+)?', ajaxviews.add_tardy),
	url(r'^add_rental/(\d+)?', ajaxviews.add_rental),
	# Search students advanced
	#url(r'^search_students/([a-zA-Z_]*)/([a-zA-Z0-9<>]*)/([0-9]*)', ajaxviews.search_students),
	# Multi search students advanced
	url(r'^search_students/([0-9]*)/', ajaxviews.search_students),
	url(r'^search_locks/([0-9]*)/', ajaxviews.search_locks),
	url(r'^get_student/get/([0-9]*)', ajaxviews.get_student),
	url(r'^update_student/([0-9]*)/([a-zA-Z0-9_]*)/([\W,a-zA-Z0-9]*)', ajaxviews.update_student),
	url(r'^get_lock/get/([0-9]*)', ajaxviews.get_lock),
	url(r'^update_lock/([0-9]*)/([a-zA-Z0-9_]*)/([a-zA-Z0-9-]*)', ajaxviews.update_lock),
	url(r'^', ajaxviews.url_error),
)