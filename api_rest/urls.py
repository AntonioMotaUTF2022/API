from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nick), # passa a string nick para a função get_by_nick
    path('data/', views.user_manager)
]
