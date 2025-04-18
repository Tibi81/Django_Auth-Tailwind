from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email_token = models.CharField(max_length=64, blank=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
