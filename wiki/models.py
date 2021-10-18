from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

TYPES = (
                 ('L', 'Locations'),
                 ('P', 'People'),
                 ('E', 'Events'),
                 ('F', 'Factions'),
                )

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return "%s (%s)" %(self.title, self.type)

    def get_absolute_url(self):
        return reverse('article', kwargs={'url_title': self.title})

class Comment(models.Model):
    text = models.CharField(max_length=100)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
