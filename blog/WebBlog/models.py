from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import Field
from django.contrib.auth.signals import user_logged_in

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeId = models.CharField(max_length=30)
    login_count = models.PositiveIntegerField(default=0)

    def login_user(sender, request, user, **kwargs):
        user.employee.login_count = user.employee.login_count + 1
        user.employee.save()

    user_logged_in.connect(login_user)