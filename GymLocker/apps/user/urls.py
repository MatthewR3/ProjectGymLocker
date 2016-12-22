from django.conf.urls import patterns, include, url

from GymLocker.apps.user import userviews


urlpatterns = patterns('',
	url(r'^logout/', userviews.logout_user),
    url(r'^login/', userviews.login_user),

)