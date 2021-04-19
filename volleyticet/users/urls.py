from django.urls import path, re_path, include

from users.views import SignupView, LoginView

urlpatterns = [
    # path('list/', views.user_list_view),
    # path('item/', views.UserListItemView.as_view()),
    # path('login/', views.login_view),
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),

    # path('', include('django.contrib.auth.urls')), # new
]