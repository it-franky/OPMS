from django.contrib import admin

import xadmin

from .models import Fitness,Cycling,Journey  # Import our todo Model.
# Register your models here.



class FitnessAdmin(object):
    list_display = ['project', 'load', 'count', 'groups','place']
    search_fields = ['project', 'load', 'count', 'groups','place']
    list_filter = ['project', 'load', 'count', 'groups','place']

class CyclingAdmin(object):
    list_display = ['riding_date', 'distance', 'duration', 'route']
    search_fields = ['riding_date', 'distance', 'duration', 'route']
    list_filter = ['riding_date', 'distance', 'duration', 'route']

class JourneyAdmin(object):
    list_display = ['state', 'city', 'start_date', 'end_date','spend']
    search_fields = ['state', 'city', 'start_date', 'end_date','spend']
    list_filter = ['state', 'city', 'start_date', 'end_date','spend']

xadmin.site.register(Fitness, FitnessAdmin)
xadmin.site.register(Cycling, CyclingAdmin)
xadmin.site.register(Journey, JourneyAdmin)
