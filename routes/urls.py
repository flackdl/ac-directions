from django.conf.urls import url, include
from routes.views import MapView, VuetifyView, DirectionsView

urlpatterns = [
    url(r'^map/$', MapView.as_view()),
    url(r'^vuetify/$', VuetifyView.as_view()),
    url(r'^directions/$', DirectionsView.as_view()),
]