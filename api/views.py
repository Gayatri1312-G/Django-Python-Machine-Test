# api/views.py
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import Client, Project
from .serializers import (
    ClientSerializer, ProjectCreateSerializer, ProjectDetailSerializer
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class ClientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, creating, retrieving, updating and deleting clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProjectCreateAPIView(generics.CreateAPIView):
    """
    API endpoint to create a project for a specific client.
    URL: /api/clients/<client_id>/projects/
    """
    serializer_class = ProjectCreateSerializer

    def create(self, request, *args, **kwargs):
        client_pk = self.kwargs.get('client_pk')
        client = get_object_or_404(Client, pk=client_pk)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Manually create the project instance
        project = Project.objects.create(
            project_name=serializer.validated_data['project_name'],
            client=client,
            created_by=request.user
        )
        project.users.set(serializer.validated_data['users'])
        
        # Use a different serializer for the output
        output_serializer = ProjectDetailSerializer(project)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MyProjectsListAPIView(generics.ListAPIView):
    """
    API endpoint to list all projects assigned to the logged-in user.
    URL: /api/projects/
    """
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return user.projects.all()