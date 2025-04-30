from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Team

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class JoinTeamForm(forms.Form):
    join_code = forms.CharField(max_length=10, label='Enter Team Join Code')
