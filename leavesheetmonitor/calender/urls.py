from django.conf.urls import url, include
from rest_framework import routers
from leavesheetmonitor.calender import views

router = routers.DefaultRouter()
router.register(r'calender', views.CalenderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]