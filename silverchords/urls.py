from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as users_views
from beats import views as beats_views
from notifis import views as noti_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('galleryouter/', users_views.galleryouter, name='gallery2'),
    path('beats/', include('beats.urls')),
    path('users/', include('users.urls')),
    path('',beats_views.silverchords, name='silverchords'),
    path('help/', users_views.helpinfofun, name='helpinfo'),
    path('notifications/list', include('notifis.urls')),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
