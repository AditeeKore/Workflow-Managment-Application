from django.shortcuts import render , HttpResponse


def index(request):
    # return HttpResponse("this is homepage")
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def faq(request):
    return render(request, 'faq.html')

def tasks(request):
    return render(request, 'tasks.html')
