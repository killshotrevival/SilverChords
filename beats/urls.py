from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from beats import views 


urlpatterns = [
    path('home/', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('history/', views.HistoryNameList.as_view(), name='history'),
    path('beat/<int:pk>/', views.BeatDetailsView.as_view(), name='beat-details'),
    path('beatlist/', views.BeatListView.as_view(), name='beat-list'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
