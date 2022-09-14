from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=512, null=True)
    rating = models.IntegerField()
    image = models.TextField(null=True)

    def __str__(self):
        suffix = f', {self.country}' if self.country else ''

        return f'{self.name}{suffix}'
