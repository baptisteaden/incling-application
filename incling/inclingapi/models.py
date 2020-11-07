from django.db import models

class Tile(models.Model):
    TileStatus = models.TextChoices('TileStatus', 'LIVE PENDING ARCHIVED')
    launchDate = models.DateField
    status = models.CharField(max_length=8, choices=TileStatus.choices)

class Task(models.Model):
    TaskType = models.TextChoices('TaskType', 'SURVEY DISCUSSION DIARY')
    title = models.CharField(max_length=50)
    order = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TaskType.choices)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE)