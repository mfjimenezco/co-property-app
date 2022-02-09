"""
Account admin register.
"""

# Django
from django.contrib import admin

# Models
from accounts.models import UserRequest


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    """User Request Admin"""
    list_display = (
        'username',
        'email',
        'is_accepted',
    )
    search_fields = (
        'username',
        'email',
    )
    list_filter = (
        'is_accepted',
    )
    list_editable = ('is_accepted',)