from django.shortcuts import render

from . models import Task
from rest_framework import viewsets
from serializers import TaskSerializer

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


