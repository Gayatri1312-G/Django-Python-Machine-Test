# webapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView,
    ClientDeleteView, ProjectCreateView, MyProjectsView
)

app_name = 'webapp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', ClientListView.as_view(), name='client-list'),
    path('clients/new/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    path('clients/<int:client_pk>/projects/new/', ProjectCreateView.as_view(), name='project-create'),
    path('my-projects/', MyProjectsView.as_view(), name='my-projects'),
]