from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('create_team/', views.create_team, name='create_team'),
    path('register/', views.register_view, name='register'),
]
