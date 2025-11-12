from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def student_dashboard(request):
    data = {
    "name": "GoUpTech",
    "attendance": 92,
    "upcoming_classes": 3
    }
    return Response(data)