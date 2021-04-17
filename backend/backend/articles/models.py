from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]