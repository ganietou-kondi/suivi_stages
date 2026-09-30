from django.db import models


class Stage(models.Model):
    sujet = models.CharField(max_length=150)
    