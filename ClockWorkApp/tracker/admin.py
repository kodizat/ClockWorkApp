from django.contrib import admin
from .models import CustomUser, Team, Habit, Progress

admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Habit)
admin.site.register(Progress)
