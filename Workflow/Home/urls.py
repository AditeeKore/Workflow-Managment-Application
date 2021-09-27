from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("userlogin", views.userlogin, name='userlogin'),
    path("register", views.register, name='register'),
    path("logout", views.user_logout, name='logout'),
    path("faq", views.faq, name='faq'),
    path("tasks", views.tasks, name='tasks'),
    path("myprofile", views.myprofile, name='myprofile'),
    path("taskassign", views.taskassign, name='taskassign'),
    path("mytask", views.mytask, name='mytask'),
]
