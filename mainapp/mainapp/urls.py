"""
mainapp URL Configuration
"""

# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Views
from mainapp import views as local_views

urlpatterns = [
    path('', local_views.home, name='home'),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    # Internationalization
    path('i18n/', include('django.conf.urls.i18n')),
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
