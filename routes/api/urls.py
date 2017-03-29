from routes.api import views
from django.conf.urls import url, include
from rest_framework import routers

default_router = routers.DefaultRouter()
default_router.register(r'routes', views.RouteViewSet)
default_router.register(r'directions', views.DirectionsViewSet)

urlpatterns = [
    url(r'^', include(default_router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
