from django.shortcuts import render , HttpResponse


def index(request):
    # return HttpResponse("this is homepage")
    return render(request, 'index.html')

def login(request):
    return HttpResponse("this is login page")

def faq(request):
    return render(request, 'faq.html')
