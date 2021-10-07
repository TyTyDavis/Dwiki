from django.db import models


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
