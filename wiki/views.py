from django.shortcuts import render
from django.http import HttpResponse
from wiki.models import Article
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView

def index(request):
    a = Article.objects.get(pk=1)
    return render(request,"home.html",{"objects" : Article.objects.all()})

def articleView(request, url_title):

    a = get_object_or_404(Article, title=url_title)
    return render(request,"article.html",{"title" : a.title, "body" : a.body, "pk" : a.pk })

class articleCreate(CreateView):
    model = Article
    fields = ['title', 'body', 'type']

class articleUpdate(UpdateView):
    model = Article
    fields = ['title', 'body', 'type']
    template_name_suffix = '_update_form'
