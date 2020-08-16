from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.views import home, register, profileDetials

urlpatterns = [
    path('', home, name='home'),
    path('signup/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profileDetials, name='profile-details'),
]
