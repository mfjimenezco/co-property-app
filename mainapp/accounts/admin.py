"""
Account admin register.
"""

# Django
from django.contrib import admin
from django.contrib import messages

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
    def save_model(self, request, obj, form, change):
        try:
            super(UserRequestAdmin, self).save_model(request, obj, form, change)
        except Exception as e:
            # Add error message
            messages.add_message(request, messages.ERROR, e)