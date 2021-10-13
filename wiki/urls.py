
from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('home/', views.index, name='home'),
    path('create/', views.articleCreate.as_view(), name='create'),
    path('edit/<int:pk>', views.articleUpdate.as_view(), name='edit'),
    path('<str:url_title>/', views.articleView, name='article'),
    path('delete/<int:pk>', views.articleDelete.as_view(), name='delete'),
    
]
