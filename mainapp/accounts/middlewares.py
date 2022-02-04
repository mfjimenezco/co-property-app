"""
Accounts middleware catalog.
"""

# Django
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class ProfileCompleteMiddleware:
    """Profile complete middleware.

    Ensures that every user using the app has their complete profile
    (first name, last name and email).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if not user.is_anonymous:
            if (not user.first_name or
                not user.last_name or
                    not user.email):
                print(request.path)
                if (not (str(request.path).startswith('/i18n')) and 
                    request.path not in [reverse('accounts:profile'),
                                        reverse('accounts:logout')]):
                    messages.warning(request,
                                     _('Please complete your profile before using the app'))
                    return redirect('accounts:profile')

        response = self.get_response(request)

        return response
