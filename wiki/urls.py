from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('<str:url_title>/', views.articleView, name="article")
]
