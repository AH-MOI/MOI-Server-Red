from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Participation
from .serializers import ParticipationSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class ParticipationViewSet(viewsets.ViewSet):

    def create(self, request):

        obj = {
            "project_id":request.data["project_id"],
            "student_id":request.data["student_id"],
            "student_area":request.data["area"],
            }
        

        serializer = ParticipationSerializer(data=obj)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response({"message":"success"})
 