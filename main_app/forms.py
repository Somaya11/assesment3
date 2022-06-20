from django import forms
from .model import ModelForm

class TaskForm(ModelForm):
    class Task:
        model= Task
        fields= '__all__'