from django.shortcuts import render , redirect
from .forms import TaskForm , UserForm
from .models import Task
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .filters import TaskFilter

# Create your views here.

@login_required(login_url='login')
def home(request):
    """ main page """
    tasks = request.user.task_set.filter(status='not done').order_by('data_created')

    myFilter = TaskFilter(request.GET , queryset=tasks)
    tasks = myFilter.qs

    context = {'tasks':tasks , 'myFilter':myFilter}
    return render(request, 'main/home.html', context)

@login_required(login_url='login')
def add_task(request):
    """ adding tasks """

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.status = 'not done'
            obj.save()

            return redirect('home')
    context = {'form': form}
    return render(request, 'main/createTask.html', context)

@login_required(login_url='login')
def done_tasks(request):
    """ done tasks mehtod"""
    tasks = request.user.task_set.filter(status='done').order_by('data_created')
    context = {'tasks':tasks , 'done' : True}
    return render(request, 'main/home.html', context)


def registerView(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request , 'main/register.html', context)


def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password = password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.info(request , "Wrong username or password")
    context = {}
    return render(request , 'main/login.html' , context)

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def add_done_tasks(request , pk):

    task = request.user.task_set.get(id = pk)
    task.status = 'done'
    task.save()
    return redirect('done_tasks')


@login_required(login_url='login')
def updateTask(request , pk):
    
    task = Task.objects.get(id = pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance = task)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.status = 'not done'
            obj.save()

            return redirect('home')
    context = {'form': form}
    return render(request, 'main/createTask.html', context)


@login_required(login_url='login')
def deleteTask(request , pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('done_tasks')