# webapp/forms.py
from django import forms
from api.models import Client, Project

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'users']
        widgets = {
            'users': forms.SelectMultiple(attrs={'class': 'form-control'})
        }