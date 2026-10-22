# Django Resume and Portfolio Website

A Django portfolio/resume website organized into apps for resume entries, skills, work process, projects, services, blog content, and contact functionality. It uses Django templates and an AdminLTE-based admin theme.

## Features visible in the code
- Resume experience and education entries
- Skills and work-process content loaded from the database
- Project and service sections
- Blog and contact apps
- Django admin customization
- Jalali date support

## Stack
- Python and Django
- Django templates
- AdminLTE 4 integration
- Jalali date utilities

## Run locally
Create and activate a Python virtual environment, install project dependencies, and configure a private development secret key. Then run:

```bash
python manage.py migrate
python manage.py runserver
```

The repository currently does not expose a root requirements file in its top-level listing, so dependency installation should be based on the packages used by the project or a pinned requirements file should be added.

## Security
The settings are development-oriented. Set a private secret key through an environment variable and configure `DEBUG` and `ALLOWED_HOSTS` before deployment.
