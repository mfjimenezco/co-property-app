"""
Accounts forms.
"""

# Django
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _

# Models
from django.contrib.auth.models import User
from .models import UserRequest


class UpdateUserForm(forms.ModelForm):
    """Update user form."""

    required_css_class = 'required'

    first_name = forms.CharField(
        label=_('First Name'),
        min_length=2,
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('First Name'),
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(
        label=_('Last Name'),
        min_length=2,
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Last Name'),
                'class': 'form-control',
            }
        )
    )
    email = forms.EmailField(
        label=_('Email'),
        help_text=_(
            'Please enter a valid email, this is used in case you forgot your password.'),
        min_length=6,
        max_length=70,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PasswordChangeForm(PasswordChangeForm):
    """Password change form."""

    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].label = _('Old Password')
        self.fields["old_password"].widget = forms.PasswordInput(
            attrs={
                'placeholder': _('Old Password'),
                "class": "form-control"
            }
        )
        self.fields["new_password1"].label = _('New Password')
        self.fields["new_password1"].widget = forms.PasswordInput(
            attrs={
                'placeholder': _('New Password'),
                "class": "form-control"
            }
        )
        self.fields["new_password2"].label = _('Confirmation New Password')
        self.fields["new_password2"].widget = forms.PasswordInput(
            attrs={
                'placeholder': _('Confirmation New Password'),
                "class": "form-control"
            }
        )

class UserRequestForm(forms.ModelForm):
    """User Request form."""
    
    username = forms.CharField(
        label=_('Username'),
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        min_length=4,
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Username'),
                'class': 'form-control',
            }
        )
    )
    email = forms.CharField(
        label=_('Email'),
        help_text=_(
            'Enter a valid email, this is used for send your default password.'),
        min_length=6,
        max_length=70,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = UserRequest
        fields = ['username', 'email']