"""
Account models.
"""

# Django Utils
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import gettext_lazy as _

# Django Validators
from django.contrib.auth.validators import UnicodeUsernameValidator

# Django Models
from django.db import models
from django.contrib.auth.models import User

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

    def save(self, *args, **kwargs):
        if self.is_accepted is None:
            super().save(*args, **kwargs)
        else:
            from_email = None
            to_email = self.email
            if self.is_accepted:
                try:
                    # User creation
                    user = User()
                    user.username = self.username
                    user.email = self.email
                    import secrets
                    pssw = secrets.token_urlsafe(10)
                    user.set_password(pssw)
                    # Save user created
                    user.save()
                except Exception as e:
                    if 'UNIQUE constraint failed' in str(e):
                        subject = _('User was not created in %(appname)s.') % {
                            'appname': settings.APP_LONG_NAME}
                        # Build non approval email
                        body = _('Hi User Requester.\n\nYour user creation '
                                 'request for %(user)s was not approved on '
                                 '%(appname)s because the username already '
                                 'exists.\n\nRegards.') % {
                            'user': self.username,
                            'appname': settings.APP_LONG_NAME
                        }
                        # Send email
                        email_message = EmailMultiAlternatives(
                            subject, body, from_email, [to_email])
                        email_message.send()
                        # Delete user request
                        self.delete()
                    raise e
                else:
                    # Build approval email with the temporary password
                    subject = _('User created in %(appname)s.') % {
                        'appname': settings.APP_LONG_NAME}
                    body = _('Hi dear New User.\n\n'
                             'Your user %(user)s has been created in '
                             '%(appname)s. Your temporary password is:\n\n\t'
                             '%(password)s\n\nPlease complete your profile '
                             'and change your password as soon as you enter '
                             'the application.\n\nRegards.') % {
                        'user': user.username,
                        'appname': settings.APP_LONG_NAME,
                        'password': pssw
                    }
                    # Send email
                    email_message = EmailMultiAlternatives(
                        subject, body, from_email, [to_email])
                    email_message.send()
                    # Delete user request
                    self.delete()
            else:
                # Build non approval email
                subject = _('User was not created in %(appname)s.') % {
                    'appname': settings.APP_LONG_NAME}
                body = _('Hi User Requester.\n\nYour user creation request '
                         'for %(user)s was not approved on %(appname)s.\n\n'
                         'Regards.') % {
                    'user': self.username,
                    'appname': settings.APP_LONG_NAME
                }
                # Send email
                email_message = EmailMultiAlternatives(
                    subject, body, from_email, [to_email])
                email_message.send()
                # Delete user request
                self.delete()
