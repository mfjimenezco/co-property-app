# django-adminlte-base
Base Django Project Using AdminLTE Template

## Requirements

- Python installed
- Pip installed

## Install and Run for development
(In Windows)
- Clone repository
- Create virtual environment in project root: `python -m venv .venv`
- Activate virtual environment: `.venv\Scripts\activate.bat`
- Install requeriments: `pip install -r requirements\local.txt`
- Go to main app folder: `cd mainapp\`
- Set the required environment variables: `set <Environment Variable>=<Value>`
- Build the data structure in database: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Compile internationalization messages: `python manage.py compilemessages`
- Run developer server: `python manage.py runserver`

## Required environment variables

### Development

Mandatory:
- DJANGO_SETTINGS_MODULE (`set DJANGO_SETTINGS_MODULE=mainapp.settings.local`)
  
If you want to set the time zone
- DJANGO_D_APP_TIME_ZONE

If you want the app to send emails:
- DJANGO_D_APP_EMAIL_BACKEND (default: 'django.core.mail.backends.smtp.EmailBackend')
- DJANGO_D_APP_EMAIL_HOST
- DJANGO_D_APP_EMAIL_USE_TLS (default: True)
- DJANGO_D_APP_EMAIL_PORT (default: 587)
- DJANGO_D_APP_EMAIL_USER
- DJANGO_D_APP_EMAIL_PASSWORD

### Test / Production
Basic:
- DJANGO_SETTINGS_MODULE (`set DJANGO_SETTINGS_MODULE=mainapp.settings.test` / `set DJANGO_SETTINGS_MODULE=mainapp.settings.production`)
- DJANGO_D_APP_SECRET_KEY
- DJANGO_D_APP_ALLOWED_HOSTS
- DJANGO_D_APP_DEBUG (default: False)
- DJANGO_D_APP_ADMIN_URL

Internationalization:
- DJANGO_D_APP_TIME_ZONE (default: 'UTC')

Database:
- DJANGO_D_APP_DB_ENGINE
- DJANGO_D_APP_DB_NAME
- DJANGO_D_APP_DB_USER
- DJANGO_D_APP_DB_PASSWORD
- DJANGO_D_APP_DB_HOST
- DJANGO_D_APP_DB_PORT

Email sender:
- DJANGO_D_APP_EMAIL_BACKEND (default: 'django.core.mail.backends.smtp.EmailBackend')
- DJANGO_D_APP_EMAIL_HOST
- DJANGO_D_APP_EMAIL_USE_TLS (default: True)
- DJANGO_D_APP_EMAIL_PORT (default: 587)
- DJANGO_D_APP_EMAIL_USER
- DJANGO_D_APP_EMAIL_PASSWORD
