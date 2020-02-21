from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employee,Role


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Employee Details", {"fields": ["first_name", "last_name", "email", "manager_id","role"]}),
    ]


class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Role Details", {"fields": ["role_name"]})
    ]

"""
class EmployeeRolesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Employee Role Details", {"fields": ["role", "employee"]})
    ]
"""

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role,RoleAdmin)
#admin.site.register(EmployeeRoles,EmployeeRolesAdmin)
