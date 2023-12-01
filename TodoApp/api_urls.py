# api_urls.py
from django.urls import path
from .api_views import (
    TaskCreateView, TaskReadOneView,
    TaskReadAllView, TaskUpdateView, TaskDeleteView
)

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create-api'),
    path('tasks/<int:pk>/', TaskReadOneView.as_view(), name='task-read-one-api'),
    path('tasks/', TaskReadAllView.as_view(), name='task-read-all-api'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update-api'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete-api'),
]
