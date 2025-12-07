from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.IntegerField()
    image = models.ImageField(upload_to='events/')
    repository = models.URLField()

    def __str__(self):
        return f'{self.name} -- {self.date}'
