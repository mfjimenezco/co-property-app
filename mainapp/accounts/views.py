"""
Accounts views.
"""

# Django
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,
                                 update_session_auth_hash)
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

# Forms
from .forms import UpdateUserForm
from .forms import PasswordChangeForm


def login_view(request):
    """Login view."""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(
                request,
                'accounts/login.html',
                {'error': _('Invalid username and password')}
            )
    return render(
        request=request,
        template_name='accounts/login.html',
        context={
            'page_title': 'Login',
        }
    )


class PasswordResetView(SuccessMessageMixin, PasswordResetView):
    """Password reset class view"""

    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject'
    success_message = _('Instructions have been sent via email to reset '
                        'your password, if an account exists with the email you entered, '
                        'you should receive them shortly.')
    success_url = reverse_lazy('accounts:login')
    extra_context = {'page_title': _('Password recovery')}


class PasswordResetConfirmView(PasswordResetConfirmView):
    """Password reset confirm class view"""

    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    extra_context = {'page_title': _('Password recovery')}


class PasswordResetCompleteView(PasswordResetCompleteView):
    """Password reset complete class view"""

    template_name = 'accounts/password_reset_complete.html'
    extra_context = {'page_title': _('Password recovery')}


@login_required
def logout_view(request):
    """Logout a user view."""

    logout(request)
    return redirect('accounts:login')


@login_required
def profile_view(request):
    """Profile view."""

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(
                request, _('Profile updated successfully'))
            return redirect('accounts:profile')
        else:
            for field in user_form.errors:
                user_form[field].field.widget.attrs['class'] += ' is-invalid'
            messages.error(request, _(
                'It was not possible to update your profile'))
    else:
        user_form = UpdateUserForm(instance=request.user)
    return render(
        request=request,
        template_name='accounts/profile.html',
        context={
            'page_title': _('User profile'),
            'user_form': user_form,
        }
    )


@login_required
def change_password_view(request):
    """Change password view."""

    if request.method == 'POST':
        pass_form = PasswordChangeForm(request.user, request.POST)
        if pass_form.is_valid():
            user = pass_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, _('Your password was updated successfully'))
            return redirect('accounts:change_password')
        else:
            for field in pass_form.errors:
                pass_form[field].field.widget.attrs['class'] += ' is-invalid'
            messages.error(request, _(
                'It was not possible to update your password'))
    else:
        pass_form = PasswordChangeForm(request.user)
    return render(
        request=request,
        template_name='accounts/change_password.html',
        context={
            'page_title': _('Change password'),
            'pass_form': pass_form,
        }
    )
