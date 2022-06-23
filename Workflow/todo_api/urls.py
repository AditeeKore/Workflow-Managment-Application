from django.conf.urls import url
from django.urls import path, include
from .views import (
    TodoDetailApiView,
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>', TodoDetailApiView.as_view()),
]