from __future__ import unicode_literals
from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.name