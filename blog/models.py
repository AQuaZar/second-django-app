from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)


# Create your models here.
