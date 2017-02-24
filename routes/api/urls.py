from routes.api import views
from django.conf.urls import url, include
from rest_framework import routers

default_router = routers.DefaultRouter()
default_router.register(r'routes', views.RouteViewSet)

#routes_router = routers.DefaultRouter()
#router.register(r'coords', views.CoordViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(default_router.urls)),
    #url(r'^route/(?P<id>\d+)/', include(routes_router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
