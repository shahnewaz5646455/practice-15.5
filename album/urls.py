from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]