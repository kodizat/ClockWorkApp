from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import Team, CustomUser, Habit
from .forms import CustomUserCreationForm, TeamForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, you can set is_team_captain or any other custom logic here
            # user.is_team_captain = False  # If you want to set default value
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')  # Redirect to dashboard or desired page
        else:
            # If the form is not valid, display form errors
            return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def dashboard(request):
    teams = Team.objects.all()  # List all teams for simplicity
    return render(request, 'dashboard.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {'team': team})

def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.captain = request.user
            team.save()
            return redirect('dashboard')
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})

def login_view(request):
    return render(request, 'tracker/login.html')

def register_view(request):
    return render(request, 'tracker/register.html')