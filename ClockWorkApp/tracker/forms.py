from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Team

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'is_team_captain']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
