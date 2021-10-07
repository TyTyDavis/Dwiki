from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.index, name='index'),
    path('<str:url_title>/', views.articleView)
]
