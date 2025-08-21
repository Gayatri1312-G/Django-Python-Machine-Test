# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectCreateAPIView, MyProjectsListAPIView

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:client_pk>/projects/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('projects/', MyProjectsListAPIView.as_view(), name='my-projects'),
]