from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# UserAdmin.fieldsets += ('Custom Field Set', {'fields': ('jim',)}),
# print(UserAdmin.fieldsets)

admin.site.register(CustomUser, UserAdmin)