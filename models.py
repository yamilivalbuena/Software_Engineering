from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#This class establishes the information to be saved to the database regarding the destinations

class Destination(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.DateTimeField(default=timezone.now)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destination-detail', kwargs={'pk': self.pk})
