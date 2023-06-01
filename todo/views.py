from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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
    template_name = "task/home.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)

        # new_task = form.save(commit=False)
        # if self.request.user.is_authenticated:
        #     new_task.user = self.request.user
        #     new_task.save()
        #     return super().form_valid(form)
