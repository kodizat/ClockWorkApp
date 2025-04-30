from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .models import Team, CustomUser, Habit
from .forms import CustomUserCreationForm, TeamForm, JoinTeamForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    my_teams = request.user.teams.all()
    return render(request, 'dashboard.html', {'teams': my_teams})


@login_required
def team_detail(request, team_id):
    try:
        team = request.user.teams.get(id=team_id)
    except Team.DoesNotExist:
        raise Http404("You are not a member of this team.")

    my_teams = request.user.teams.all()
    habits = Habit.objects.filter(team=team)
    return render(request, 'team_detail.html', {
        'team': team,
        'my_teams': my_teams,
        'habits': habits
    })


@login_required
def join_team(request):
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['join_code']
            try:
                team = Team.objects.get(join_code=code)
                if request.user not in team.members.all():
                    team.members.add(request.user)
                    messages.success(request, f"You've joined {team.name}!")
                else:
                    messages.info(request, f"You are already a member of {team.name}.")
                return redirect('dashboard')
            except Team.DoesNotExist:
                messages.error(request, "Invalid join code.")
    else:
        form = JoinTeamForm()
    return render(request, 'join_team.html', {'form': form})


@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.captain = request.user
            team.save()
            team.members.add(request.user)  # Auto-add creator to the team
            messages.success(request, f"Team '{team.name}' created successfully.")
            return redirect('dashboard')
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})

def create_team(request):
    return render(request, 'create_team.html')

def join_team(request):
    return render(request, 'join_team.html')