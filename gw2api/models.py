from django.db import models


class World(models.Model):
    world_id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    def __unicode__(self):
        return self.name


class Match(models.Model):
    match_id = models.CharField(primary_key=True, max_length=10)
    red = models.ForeignKey(World, related_name="red_world_id")
    blue = models.ForeignKey(World, related_name="blue_world_id")
    green = models.ForeignKey(World, related_name="green_world_id")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return self.match_id