from django.urls import path
from django.contrib.auth import views as auth_views
from tracker import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),  # This includes the Django admin URL
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('create_team/', views.create_team, name='create_team'),
    path('register/', views.register, name='register'),
    path('join-team/', views.join_team, name='join_team'),
]
