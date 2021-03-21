from django.contrib import admin
from .models import Voter,Contestant
admin.site.register(Contestant)

# Register your models here.
class VoterAdmin (admin.ModelAdmin):
    list_per_page = 7000
admin.site.register(Voter,VoterAdmin)