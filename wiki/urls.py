from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('<str:url_title>/', views.articleView, name='article')
]
