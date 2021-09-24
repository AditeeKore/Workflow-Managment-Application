from django.shortcuts import render, redirect, HttpResponse
from Home.models import Assigned_tasks
from django.contrib import messages
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.admin.views.decorators import staff_member_required




def index(request):
    # return HttpResponse("this is homepage")
    return render(request, 'index.html')

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are mnow logged in as {username}.")
                return redirect('/index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()          
    return render(request, 'userlogin.html', {"login_form":form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/index')


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/index')
        messages.error(request, "Registration is unsuccessful.")
    form = NewUserForm()
    return render(request, "register.html", {'register_form': form})
   

def faq(request):
    return render(request, 'faq.html')

# @login_required(login_url='/admin/login/?next=/admin/')
# @staff_member_required
def tasks(request):
    task_list = Assigned_tasks.objects.all()
    return render(request, 'tasks.html', {'task_list': task_list})

# @login_required(login_url='/admin/login/?next=/admin/')
# @staff_member_required
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

def mytask(request):
    return render(request, 'mytask.html')

def myprofile(request):
    return render(request, 'myprofile.html')



