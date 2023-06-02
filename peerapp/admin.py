from django.contrib import admin
from .models import Person, Rating, Team

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Rating)

