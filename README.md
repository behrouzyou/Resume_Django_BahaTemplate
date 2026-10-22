# Django Resume and Portfolio Website

A Django portfolio/resume website organized into apps for resume entries, skills, work process, projects, services, blog content, and contact functionality. The project uses Django templates and an AdminLTE-based Django admin theme.

## Features visible in the code
- Resume experience and education entries
- Skills and work-process content loaded from the database
- Project and service sections
- Blog and contact apps
- Django admin customization
- Jalali date support

## Tech stack
- Python and Django
- Django templates
- AdminLTE 4 integration
- django-jalali-date

## Run locally
Requires Python and pip.

```bash
git clone https://github.com/behrouzyou/Resume_Django_BahaTemplate.git
cd Resume_Django_BahaTemplate
python -m venv .venv
```

Activate the environment and install the project's dependencies. Configure a local Django secret key and allowed hosts, then run:

```bash
python manage.py migrate
python manage.py runserver
```

## Security
The current settings are development-oriented. Set a private secret key through an environment variable and configure `DEBUG` and `ALLOWED_HOSTS` appropriately before deployment.
