from django.contrib import admin

from drons.models import DroneCategory, Drone, Pilot, Competition

drones_models = [Drone, DroneCategory, Pilot, Competition]
admin.site.register(drones_models)
