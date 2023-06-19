from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    task_list = Task.objects.all()
    context = {'task_list' : task_list}
    return render(request, 'task/home.html', context)


def generate(request):
    task_list = Task.objects.order_by("date_created")
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TaskForm()
    context = {'form' : form, 'task_list' : task_list}
    return render(request, 'task/generate.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    # form = TaskForm()
    context = {'form' : form, 'task' : task}
    return render(request, 'task/update.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('home')