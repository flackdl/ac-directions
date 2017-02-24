from django.conf.urls import url, include
from django.contrib import admin
from routes import urls as route_urls
from routes.api import urls as api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^routes/', include(route_urls)),
    url(r'^api/', include(api_urls)),
]
