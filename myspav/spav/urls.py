from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faculty/', views.faculty, name='faculty'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
]
