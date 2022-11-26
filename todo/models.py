from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.

class task(models.Model):
    date=models.DateField(default=datetime.utcnow)
    title=models.CharField(max_length=100)
    details=models.TextField()

    def __str__(self):
        return f"{self.date}-{self.title}"

    def get_absolute_url(self):
        return reverse('task-view')
