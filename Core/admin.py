from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User

@admin.register(User)
class BaseUserAdmin(UserAdmin):
    pass


# Register your models here.
