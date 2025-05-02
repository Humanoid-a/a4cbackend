from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School
from .models import FrontendUser

@admin.register(FrontendUser)
class FrontendUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {
            'fields': ('biography', 'profile_picture')
        }),
    )

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_id')
    search_fields = ('name', 'school_id')
