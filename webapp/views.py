# webapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from api.models import Client, Project
from .forms import ClientForm, ProjectForm

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'webapp/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'webapp/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'webapp/client_form.html'
    success_url = reverse_lazy('webapp:client-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'webapp/client_form.html'
    success_url = reverse_lazy('webapp:client-list')

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'webapp/client_confirm_delete.html'
    success_url = reverse_lazy('webapp:client-list')

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'webapp/project_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.client = get_object_or_404(Client, pk=self.kwargs['client_pk'])
        return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.client = self.client
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('webapp:client-detail', kwargs={'pk': self.client.pk})

class MyProjectsView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'webapp/my_projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return self.request.user.projects.all()