from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from ..participation.models import Participation 
from ..participation.serializers import ParticipationSerializer
from django.db.models import Avg, Max, Min, Sum, Count

import json

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
            }


        serializer = ProjectSerializer(data=obj)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.filter(pk=pk)
        serializer = ProjectSerializer(queryset.values()[0])

        personnel = queryset.values()[0]["personnel"].split("|")
        personnels = []
        
        for i in personnel :
            partandpeople = i.split("/")
            
            obj = { "part" : partandpeople[0],
                    "total" : int(partandpeople[1]),
                    "cur_people" : 2 }
            personnels.append(obj)

        data = {"personnels":personnels}
        data.update(serializer.data)
        return Response(data)
