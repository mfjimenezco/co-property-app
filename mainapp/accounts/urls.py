"""
Account urls.
"""

# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    path(route='login/',
         view=views.login_view,
         name='login'),
    path(route='logout/',
         view=views.logout_view,
         name='logout'),
    path(route='profile/',
         view=views.profile_view,
         name='profile'),
    path(route='change-password/',
         view=views.change_password_view,
         name='change_password'),
    path(route='password-reset/',
         view=views.PasswordResetView.as_view(),
         name='password_reset'),
    path(route='password-reset-confirm/<uidb64>/<token>/',
         view=views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path(route='password-reset-complete/',
         view=views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path(route='user-request/',
         view=views.CreateUserRequestView.as_view(),
         name='user_request'),
]
