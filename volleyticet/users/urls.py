from django.urls import path, re_path, include

from users.views import SignupView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
]