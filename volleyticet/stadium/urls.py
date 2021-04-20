from django.urls import path, re_path, include

from stadium.views import AddStadiumView, SeatsView

urlpatterns = [
    path('addstadium/', AddStadiumView.as_view()),
    path('seats/', SeatsView.as_view()),
]