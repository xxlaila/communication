from django.contrib import admin

# Register your models here.
from .models.users import *

class UsersAdmin(admin.ModelAdmin):
    name_hierarchy = 'username'

    list_display = (
        'id', 'username', 'password', 'realname', 'sex', 'email', 'mobile', 'is_active', 'date_created')
    ordering = ('username',)
    fk_fields = ('username')
    search_fields = ("username", "realname", "sex")
    list_per_page = 25

admin.site.register(Users, UsersAdmin)
