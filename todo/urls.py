from django.urls import path
from .views import TaskListView, CreateTaskView, DeleteTaskView, DownTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('create/', CreateTaskView.as_view(), name="task_create"),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name="task_delete"),
    path('down/<int:pk>/', DownTaskView.as_view(), name="task_down"),
]
