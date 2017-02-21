from django.conf.urls import url, include
from routes.views import ImportRoute

urlpatterns = [
    url(r'^process/files', ImportRoute.as_view()),
]