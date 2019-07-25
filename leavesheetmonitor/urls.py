from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^calender/', include('leavesheetmonitor.leaves.urls')),
    url(r'^calender/', include('leavesheetmonitor.calender.urls')),
    url(r'^calender/', include('leavesheetmonitor.holidays.urls')),
    url(r'^support/', include('leavesheetmonitor.tickets.urls')),
    url(r'^users/', include('leavesheetmonitor.users.urls')),
]

