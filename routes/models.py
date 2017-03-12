from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Route(models.Model):
    name = models.CharField(max_length=60)
    coords = ArrayField(models.CharField(max_length=255), default=list())
    
    def __unicode__(self):
        return self.name