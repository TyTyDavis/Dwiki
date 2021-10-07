
from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('create/', views.articleCreate.as_view(), name='create'),
    path('<str:url_title>/', views.articleView, name='article'),
]
