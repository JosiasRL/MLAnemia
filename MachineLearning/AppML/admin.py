from django.contrib import admin
from .models import Profile

# Register your models here.
""" 
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user__name", "user__group", "first_name","last_name")
    search_fields = ("user__name", "user__groups__name", "last_name")
    list_filter = ("user__group")
    
    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])
    
    user_group.short_description = "Grupo"
"""
admin.site.register(Profile)
