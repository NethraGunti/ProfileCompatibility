from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.views import home, register, profileDetials, question1, question2, question3, compatibility, editProfile

urlpatterns = [
    path('', home, name='home'),
    path('signup/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profileDetials, name='profile-details'),
    path('questions/1', question1, name='question1'),
    path('questions/2', question2, name='question2'),
    path('questions/3', question3, name='question3'),
    path('compatibility/', compatibility, name='compatibility'),
    path('edit-profile/', editProfile, name='edit-profile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)