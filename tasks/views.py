from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm() 

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') 


    return render(request, 'tasks/list.html', context={'tasks':tasks, 'form':form})

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'tasks/update_task.html', context={'form':form})


def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'tasks/delete_task.html', context={'item': item})