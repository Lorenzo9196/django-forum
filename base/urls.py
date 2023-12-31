from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.registerLogin, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('room/<int:pk>/', views.room, name='room'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<int:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<int:pk>/', views.deleteMessage, name='delete-message'),
]
