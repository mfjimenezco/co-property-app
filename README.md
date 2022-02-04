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
- Set the required environment variables: `set DJANGO_SETTINGS_MODULE=mainapp.settings.local`, `set DJANGO_D_APP_EMAIL_USER=<email_to_send>`, `set DJANGO_D_APP_EMAIL_PASSWORD=<email_password>`
- Build the data structure in database `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Compile internationalization messages `python manage.py compilemessages`
- Run developer server: `python manage.py runserver`
