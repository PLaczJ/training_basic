from django.db import models

from django.db.models import Model


class ModelDemo(Model):
    name = models.JSONField()
