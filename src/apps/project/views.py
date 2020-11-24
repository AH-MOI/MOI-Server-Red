from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404

class ProjectViewSet(viewsets.ViewSet):

    def list(self,request):

        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset,many=True)

        return Response(serializer.data)

    def create(self, request):

        obj = {
            "title":request.data["title"], 
            "content":request.data["content"],
            "closing_date":request.data["closing_date"],
            "writer":request.data["writer"], 
            "personnel":request.data["personnel"],
            "hashtag":request.data["hashtag"],
            "profile":request.data["profile"]
            }


        serializer = ProjectSerializer(data=obj)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
