from django.urls import path
from .views import CustomLoginView, SingUpUserView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="/"), name="logout"),
    path("singup/", SingUpUserView.as_view(), name="signup"),
]