from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from apps.project.views import ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"",ProjectViewSet, basename="project")


urlpatterns = [
    url(r"^", include(router.urls)),
]