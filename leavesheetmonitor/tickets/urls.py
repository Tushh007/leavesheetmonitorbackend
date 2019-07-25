from django.conf.urls import url, include
from rest_framework import routers
from leavesheetmonitor.tickets import views

router = routers.DefaultRouter()
router.register(r'tickets', views.TicketsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^tickets-auth/', include('rest_framework.urls', namespace='rest_framework')),
]