from django.shortcuts import render
from django.http import HttpResponse
from wiki.models import Article


def index(request):
    a = Article.objects.get(pk=1)
    return render(request,"hello.html",{"title" : a.title, "body" : a.body})
