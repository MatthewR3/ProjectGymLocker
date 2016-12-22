from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    # Regex matches login or logout
    url(r'^user/', include('GymLocker.apps.user.urls')),
    url(r'^ajax/', include('GymLocker.apps.main.ajaxurls')),
    url(r'^', include('GymLocker.apps.main.urls')),

]
