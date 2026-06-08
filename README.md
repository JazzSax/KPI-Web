# KPI-Web

Small Django web application for tracking Key Performance Indicators (KPIs).

## Quick overview

- Django project root: `manage.py` and `mysite/` settings.
- Apps included: `accounts/`, `kpi_web_app/`.
- Custom management commands: `load_accounts` and `load_kpis` (see each app's `management/commands`).
- Templates in `templates/` and app-level `templates/` folders.
- Static assets under `static/` (CSS, JS, images).

## Prerequisites

- Python 3.8+ (use the version you prefer)
- pip
- Recommended: create a virtual environment

## Setup (Windows PowerShell)

1. Create and activate a virtual environment

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies

   If a `requirements.txt` file exists:

   ```powershell
   pip install -r requirements.txt
   ```

   Otherwise at minimum install Django:

   ```powershell
   pip install django
   ```

3. Apply migrations

   ```powershell
   python manage.py migrate
   ```

4. (Optional) Create a superuser

   ```powershell
   python manage.py createsuperuser
   ```

5. Run the development server

   ```powershell
   python manage.py runserver
   ```

6. Run tests

   ```powershell
   python manage.py test
   ```

## Useful management commands

- Load sample/accounts data: `python manage.py load_accounts`
- Load KPI data: `python manage.py load_kpis`

## Project layout (important files)

- `manage.py` — Django CLI entrypoint
- `mysite/settings.py` — project settings
- `accounts/` — user and account management app
- `kpi_web_app/` — KPI models, views and templates
- `static/` — CSS/JS/images
- `templates/` — base templates

## Notes

- Add a `requirements.txt` to record project dependencies.
- If deploying to production, configure `ALLOWED_HOSTS`, use a proper WSGI server, and set `DEBUG=False`.

## License
