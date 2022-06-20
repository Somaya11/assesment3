from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index (request):
    all_tasks = Task.objects.all() 
    form = TaskForm()
    return render(request, 'index.html', {'all_tasks': all_tasks, 'form': form})


def addTask(request):
    form = TaskForm(request.POST)
    form.save()
    return redirect('index')
