from django.contrib import admin
from django.contrib.auth import get_user_model, admin as auth_admin

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'role')
