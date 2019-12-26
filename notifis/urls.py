from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from notifis import views


urlpatterns = [ 
    path('list/', views.notificationListView.as_view(), name='notification'), 
    path('deletenoti/<int:pk>', views.delete, name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)