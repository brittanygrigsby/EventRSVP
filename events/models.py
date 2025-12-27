from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='events/')
    registry_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f'{self.name} -- {self.date}'
