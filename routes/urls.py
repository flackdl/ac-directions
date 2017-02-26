from django.conf.urls import url, include
from routes.views import MapView

urlpatterns = [
    url(r'^map/$', MapView.as_view()),
]