from django.urls import path

from .views import *

urlpatterns = [
    path("<id>", GetProjectAPI.as_view()),
    path("", ListProjectAPI.as_view()),
]
