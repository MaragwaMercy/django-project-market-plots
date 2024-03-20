from django.contrib import admin
from .models import Plots, Owner, Ownership, AdministrationPlanning, Infrastructure

# Register your models here
admin.site.register(Plots)
admin.site.register(Owner)
admin.site.register(Ownership)
admin.site.register(AdministrationPlanning)
admin.site.register(Infrastructure)
