from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')


class Category(models.Model):
    title = title = models.CharField(max_length=20)
