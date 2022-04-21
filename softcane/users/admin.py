from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AdminUserForm, CustomAdminUserChangeForm
from .models import User

class AdminUserForm(UserAdmin):
    add_form = AdminUserForm
    form = CustomAdminUserChangeForm
    model = User
    list_display = ['username', 'fullname', 'email', 'department','designation', 'is_active']

admin.site.register(User, UserAdmin)