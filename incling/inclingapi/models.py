from django.db import models


class Tile(models.Model):
    TILE_STATUSES = (
        ('live', 'Live'),
        ('pending', 'Pending'),
        ('archived', 'Archived')
    )
    launchDate = models.DateField()
    status = models.CharField(max_length=8, choices=TILE_STATUSES)


class Task(models.Model):
    TASK_TYPES = (
        ('survey', 'Survey'),
        ('discussion', 'Discussion'),
        ('diary', 'Diary')
    )
    title = models.CharField(max_length=50)
    order = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=10, choices=TASK_TYPES)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)
