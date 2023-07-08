from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Register your models here.
# ID: luiscarbogniani pass: probando123

admin.site.register(User)
admin.site.register(AbstractUser)