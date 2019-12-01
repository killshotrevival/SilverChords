from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as users_views


urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('editinfo/', users_views.edit, name='editinfo'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),    
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
