from django.shortcuts import render
from django.views.generic import ListView, CreateView

from todo.forms import CreatTaskForm
from todo.models import Task


class TaskListView(ListView):
    template_name = "todo/home.html"
    context_object_name = "tasks"

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.all().filter(user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatTaskForm()
        return context
