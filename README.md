# django-adminlte-base
Base Django Project Using AdminLTE Template

## Requirements

- Python installed
- Pip installed

## Install and Run

- Clone repository
- Create virtual environment in project root: `virtualenv -p $(which python3) .venv` (unix based) or `python -m venv .venv` (windows)
- Activate virtual environment: `.venv\Scripts\activate.bat`
- Install requeriments: `pip install -r requirements\local.txt`
- Go to main app folder: `cd mainapp\`
- Build the data structure in database `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Compile internationalization messages `python manage.py compilemessages`
- Run developer server: `python manage.py runserver`
