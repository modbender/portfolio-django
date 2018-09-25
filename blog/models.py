from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pdate = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def trim(self):
        return self.body[:10]+"..."

    def ago(self):
        return self.pdate.strftime('%b %e %Y')
