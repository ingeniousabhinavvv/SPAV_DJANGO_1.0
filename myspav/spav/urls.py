from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faculty/', views.faculty, name='faculty'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('downloads/', views.downloads, name='downloads'),
    path('search/', views.search, name='search'),
]
