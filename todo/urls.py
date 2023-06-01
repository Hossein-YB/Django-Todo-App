from django.urls import path
from .views import TaskListView, CreateTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('create/', CreateTaskView.as_view(), name="task_create"),
]
