from django.contrib import admin

from .models import GSCapabilitySet, GSInstance, GSGroup, GSUser

# Register your models here.
admin.site.register(GSCapabilitySet)
admin.site.register(GSInstance)
admin.site.register(GSGroup)
admin.site.register(GSUser)

