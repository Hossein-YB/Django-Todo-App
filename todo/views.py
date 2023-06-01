from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from todo.forms import CreatTaskForm
from todo.models import Task


class TaskListView(LoginRequiredMixin, ListView):
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


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('task', 'task_description')
    template_name = "todo/home.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        new_task = form.save(commit=False)
        if self.request.user.is_authenticated:
            new_task.user = self.request.user
            new_task.save()
            return super().form_valid(form)

    def form_invalid(self, form):
        return redirect("task_list")


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
