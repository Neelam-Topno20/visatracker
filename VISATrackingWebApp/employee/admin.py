from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Employee, Role, ApplicationStatus, EmailContent, VisaApplication, ApplicationHistory, EmailLog


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Employee Details", {"fields": ["first_name", "last_name", "email", "manager_id","role"]}),
    ]


class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Role Details", {"fields": ["role_name"]})
    ]


class ApplicationStatusAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Application Status",{"fields":["status"]})
    ]

class EmailContentAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Email Content",{"fields":["content","status_id"]})
    ]


class VisaApplicationAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Application Details",{"fields":["employee_id","status_id","initiated_by","action_pending_on"]})
    ]


class ApplicationHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Application History", {"fields": ["application_id" ]})
    ]


class EmailLogAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Email Log Details",{"fields":["application_history_id"]})
    ]


"""
class EmployeeRolesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Employee Role Details", {"fields": ["role", "employee"]})
    ]
"""

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)
admin.site.register(EmailContent, EmailContentAdmin)
admin.site.register(VisaApplication, VisaApplicationAdmin)
admin.site.register(ApplicationHistory, ApplicationHistoryAdmin)
admin.site.register(EmailLog, EmailLogAdmin)
#admin.site.register(EmployeeRoles,EmployeeRolesAdmin)
