from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DirectorsActors(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # image =
