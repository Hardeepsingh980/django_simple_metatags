from django.db import models

class MetaTag(models.Model):
    slug = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    index = models.BooleanField(default=True)
    follow = models.BooleanField(default=True)

    def __str__(self):
        return self.slug