"""
mainapp base Views.
"""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


@login_required
def home(request):
    """Home view."""
    return render(request, 'home.html', {'page_title': _('Home')})
