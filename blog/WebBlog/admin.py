from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

    def employee_id(self, instance):
        return instance.employee.employeeId

    def login_count(self, instance):
        return instance.employee.login_count

    list_display = ('username', 'first_name', 'last_name',
                'is_active', 'employee_id', 'login_count')



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
