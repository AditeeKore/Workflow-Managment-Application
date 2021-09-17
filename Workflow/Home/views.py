from django.shortcuts import render , HttpResponse
from Home.models import Assigned_tasks
from django.contrib import messages
from .models import *
from .forms import CreateUserForm


def index(request):
    # return HttpResponse("this is homepage")
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def mytask(request):
    return render(request, 'mytask.html')


def register(request):
    form = CreateUserForm()
    if request=='POST':
        form = CreateUserForm(request.POST)
        form.save()
    
    context={'form':form}
    return render(request, 'register.html',context)

def faq(request):
    return render(request, 'faq.html')

def tasks(request):
    task_list = Assigned_tasks.objects.all()
    return render(request, 'tasks.html', {'task_list': task_list})

def taskassign(request):
    if request.method == "POST":
        task_no = request.POST.get('task_no')
        task_name = request.POST.get('task_name')
        task_desc = request.POST.get('task_desc')
        assigned_to = request.POST.get('assigned_to')
        submit_time = request.POST.get('submit_time')
        submit_date = request.POST.get('submit_date')
        taskassign=Assigned_tasks(task_no=task_no, task_name=task_name, task_desc=task_desc, assigned_to=assigned_to, 
        submit_time=submit_time, submit_date=submit_date)
        taskassign.save()
        messages.success(request, 'New task assigned')
    return render(request, 'taskassign.html')





