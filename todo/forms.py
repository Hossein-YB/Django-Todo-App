from django import forms

from todo.models import Task


class CreatTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'task_description']

