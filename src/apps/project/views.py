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

        search = request.GET.get('search' , None)
        part = request.GET.get('part',None)
        tags = request.GET.get('tags',None)

        queryset = Project.objects.all()
        
        
        if search != None :
            queryset = queryset.filter(title__icontains=search)
            
        if part != None :
            for p in part.split("+"):
                queryset = queryset.filter(personnel__icontains=p)
                
        if tags != None :
            for tag in tags.split("+"):
                queryset = queryset.filter(hashtag__icontains=tag)
            

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
        queryset = Project.objects.get(pk=pk)
        personnel = queryset.personnel.split("|")
        personnels = []
        

        for i in personnel[:-1] :
            partandpeople = i.split("/")
            cur_people = Participation.objects.filter(student_area=partandpeople[0]).aggregate(Count('id'))["id__count"]
            
            obj = { "part" : partandpeople[0],
                    "total" : int(partandpeople[1]),
                    "cur_people" : cur_people }
            personnels.append(obj)

        hashtag = queryset.hashtag.split("#")[1:]

        queryset.personnel = personnels
        queryset.hashtag = hashtag
        
        serializer = ProjectSerializer(queryset)

        
        return Response(serializer.data)
