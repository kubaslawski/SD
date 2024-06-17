from django.urls import path, re_path
from SDApp.views import (
    CustomUserRegisterView, 
    CustomUserLoginView
)

urlpatterns = [
    path("register/", CustomUserRegisterView.as_view()),
    path("login/", CustomUserLoginView.as_view()),
]
