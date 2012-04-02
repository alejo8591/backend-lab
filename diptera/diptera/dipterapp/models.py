from django.db import models

class Article(models.Model):
      title = models.CharField(max length = 64)
      content = models.TextField()


# Create your models here.
