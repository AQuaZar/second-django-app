from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"pk": self.pk})


# Create your models here.
