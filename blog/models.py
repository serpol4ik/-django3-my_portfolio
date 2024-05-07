from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title