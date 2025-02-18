from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_team_captain = models.BooleanField(default=False)

    # Adding related_name to avoid clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Changed related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Changed related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )


class Team(models.Model):
    name = models.CharField(max_length=100)
    captain = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Habit(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Progress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    progress = models.FloatField()
