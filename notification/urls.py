from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from notification import views


urlpatterns = [ 
    path('list/', views.notificationListView.as_view(), name='notification'),  
    path('notidata/', views.notidata, name='notidata'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)