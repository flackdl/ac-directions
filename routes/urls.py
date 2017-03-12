from django.conf.urls import url, include
from routes.views import MapView, VuetifyView

urlpatterns = [
    url(r'^map/$', MapView.as_view()),
    url(r'^vuetify/$', VuetifyView.as_view()),
]