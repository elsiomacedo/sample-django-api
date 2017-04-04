"""
    API Models
"""
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class SampleModel(models.Model):
    """
        Sample Model
    """
    description = models.TextField(max_length=100, null=False)
    value_x = models.FloatField(null=False)
    value_y = models.FloatField(null=False)
