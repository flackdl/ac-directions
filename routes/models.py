from __future__ import unicode_literals
from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.name
        

class Coord(models.Model):
    route = models.ForeignKey(Route, related_name='coords')
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    def __unicode__(self):
        return '%s,%s' % (self.latitude, self.longitude)