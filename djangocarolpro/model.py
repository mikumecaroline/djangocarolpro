from django.db import models


class Fashions(models.Model):
    Trousers = models.CharField(max_length=50, blank=True, null=False)
    shoes = models.CharField(max_length=50, blank=True, null=False)
    blouses = models.CharField(max_length=50, blank=True, null=False)
    dresses = models.CharField(max_length=50, blank=True, null=False)
    handbags = models.CharField(max_length=50, blank=True, null=False)


def __str__(self):
    return self.name
