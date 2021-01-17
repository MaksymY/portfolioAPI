from rest_framework import generics
from rest_framework import mixins

from adminportfolio.models import Project
from adminportfolio.api.serializers import ProjectSerializer

class ProjectItemList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset =  Project.objects.all()
