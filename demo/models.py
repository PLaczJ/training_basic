from django.db import models

from django.db.models import Model


class Chicken(Model):
    name = models.JSONField()
