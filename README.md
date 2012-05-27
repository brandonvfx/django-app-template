#{{ app_name|title }}
{% if False %}

## Starting an app

python manage.py startapp --template=https://github.com/brandonvfx/django-app-template/zipball/master --extension=py,md <app_name>

{% endif %}

## Install

###settings.py

    INSTALLED_APPS = (
        ...
        {{ app_name }}  
    )