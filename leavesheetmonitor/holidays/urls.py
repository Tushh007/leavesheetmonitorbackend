from django.conf.urls import url, include
from rest_framework import routers
from leavesheetmonitor.holidays import views

router = routers.DefaultRouter()
router.register(r'holidays', views.HolidaysViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]