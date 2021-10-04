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
    create_date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):
        return "%s (%s)" %(self.title, self.type)
