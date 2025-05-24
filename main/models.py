from django.db import models
from django.contrib.auth.models import User

class Profile_db(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='Profile_picture/', default="Profile_picture/user.png", null=True, blank=True)

    def __str__(self):
        return f"This is {self.user.username}'s profile. Email: {self.user.email}"
