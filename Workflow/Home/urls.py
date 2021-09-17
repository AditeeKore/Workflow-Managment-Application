from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("faq", views.faq, name='faq'),
    path("tasks", views.tasks, name='tasks'),
    path("mytask", views.mytask, name='mytask'),
    path("taskassign", views.taskassign, name='taskassign'),

]
