from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from apps.participation.views import ParticipationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"",ParticipationViewSet, basename="participation")


urlpatterns = [
    url(r"^", include(router.urls)),
]