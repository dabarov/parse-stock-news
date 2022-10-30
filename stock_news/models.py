from django.db import models


class StockNews(models.Model):
    category = models.CharField(max_length=20)
    published_time = models.DateTimeField()
    headline = models.CharField(max_length=255)
    image = models.URLField(blank=True)
    related = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    summary = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.headline
