from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("task_list")


class SingUpUserView(CreateView):
    model = get_user_model()
    template_name = "accounts/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("task_list")
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task_list")
        return super().get(*args, **kwargs)
