from django.contrib import admin

from .models import keys,notaCount,taskid
# Register your models here.
admin.site.register(keys)
admin.site.register(notaCount)
admin.site.register(taskid)