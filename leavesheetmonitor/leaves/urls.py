from django.conf.urls import url, include
from rest_framework import routers
from leavesheetmonitor.leaves import views

router = routers.DefaultRouter()
router.register(r'leaves', views.LeavesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]