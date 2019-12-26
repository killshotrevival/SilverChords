from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from beats import views 


urlpatterns = [
    path('home/', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('upload/', views.upload, name='upload'),
    path('history/', views.HistoryNameList.as_view(), name='history'),
    path('beat/<int:pk>/', views.beatdetails, name='beat-details'),
    path('cart/<int:pk>/', views.beatcart, name='cart'),
    path('cartdetails/', views.cartdetails, name='detailcart'),
    path('cartdelete/<int:pk>', views.cartdelete, name='deletecart'),
    path('listens/<int:pk>', views.listensupdate, name='listensupdate'),
    path('play/', views.playsonng, name='playsong'),
    path('histdetail/<int:pk>', views.historydetail, name='historydetail'),
    path('search/', views.search,name='search'),
    path('beatlist/', views.BeatListView.as_view(), name='beat-list'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
