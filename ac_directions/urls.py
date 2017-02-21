from django.conf.urls import url, include
from django.contrib import admin
from routes import urls as route_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^routes/', include(route_urls)),
]
