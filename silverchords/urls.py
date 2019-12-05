from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as users_views
from beats import views as beats_views
from notification import views as noti_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('beats/', include('beats.urls')),
    path('users/', include('users.urls')),
    path('',beats_views.silverchords, name='silverchords'),
    path('notifications/list', include('notification.urls')),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
