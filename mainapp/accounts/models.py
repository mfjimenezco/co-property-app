"""
Account models.
"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Validators
from django.contrib.auth.validators import UnicodeUsernameValidator

# Models
from mainapp.models import BaseModel


class UserRequest(BaseModel):
    """User Request Model."""

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'),
    )
    is_accepted = models.BooleanField(
        _('accepted status'),
        null=True,
        help_text=_('Designates whether the user request is accepted.'),
    )

    class Meta(BaseModel.Meta):
        """Meta class."""
        
        verbose_name = _("User Request")
        verbose_name_plural = _("User Requests")

    def __str__(self):
        return self.username
