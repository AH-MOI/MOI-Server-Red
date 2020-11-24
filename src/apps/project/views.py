from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Project
from .serializers import ProjectSerializer


class GetProjectAPI(generics.ListAPIView):

    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Project.objects.get(id=self.kwargs["id"])
    