from django.db import models

class User(models.Model):
    user_nickname = models.CharField(max_length=100, primary_key=True, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.CharField(max_length=100, default='')
    user_age = models.CharField(max_length=2, default=0)

    def __str__(self):
        return f'Nickname {self.user_nickname} / Email: {self.user_email}'

# Create your models here.
