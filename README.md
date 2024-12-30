## Django Important Notes
It is ridiculously fast, exceedingly scalable and secure framework to develop backend-applications. Use `pip install uv` as package manager, written in rust. Create a virtual environment using `uv venv`. Activate it using `source .venv\bin\activate` or `.venv\Scripts\activate`. Use django using command `uv pip install Django`. Add `django-html and html` as key-value pair for emmet setting.

### Tailwind Setup and Configuration
`python -m ensurepip --upgrade` or `python -m pip install --upgrade pip` to install pip into your venv. Use command `uv pip install django-tailwind | uv pip install django-tailwind[reload]` to install pip. Follow steps accordingly:
1. Add *tailwind* and **django_browser_reload** in Settings > Installed Apps. Run `python manage.py tailwind init` to install required dependencies.

2. Add variable `TAILWIND_APP_NAME = 'theme'` above middleware.

3. Add variable `INTERNAL_IPS = ['127.0.0.1']` for custom domain mapping.

4. Run `python manage.py tailwind install` to install the tailwind app created.

5. To use tailwind, keep `python manage.py tailwind start` command running in another terminal. Add NPM_BIN_PATH = `path/to/include/search/where npm`

6. Also add middleware, `django_browser_reload.middleware.BrowserReloadMiddleware`. Add a new path `path("__reload__/", include("django_browser_reload.urls"))`.

### File Structure and Installation
Start new project using `django-admin startproject Django_Project_Name`, Run server using `python manage.py runserver Port_Number`.
RootLevel > (ProjectLevel + manage.py (handles environment variables and starting point of application) + db.sqlite3 (default database used) + templates (html files) + static (css files)). ProjectLevel > __pycache__ + __init__.py + asgi.py + settings.py (project configuration) + urls.py (project routing) + wsgi.py

Flow: User Request - Django - URL Resolver - Urls.py - Views.py - Models.py (contacts database).
Views contains the function which returns or we can say render custom-web-pages hitting the request url. You cannot directly use static assets in your html, we need to inject your code into template engine using `{% static "style.css" %}`, also use `{% load static %}` at start of your file. Do inject following code in the STATICFILES_DIR path as `[os.path.join(BASE_DIR, "static/")]`.

### Implementing modularity using Apps
Use `python manage.py startapp App_Name` to create a new app at project level. You can redirect urls.py to app > urls.py using `path('newApp/', include('newApp.urls')),`. App helps to give modular approach to code writing, we can also create templates, but, if it doesnot found any html files, it will move up in hierarchy to look for the same.

To promote reuse, we use Block element (unnamed) present in template, such as `{% block content %}{% endblock %}`. We can import layout.html file into our custom .html file, to render html structure using following code: `{% extends "layout.html" %} {% block title %} Home Page {% endblock %}` 

### Django Admin Panel
Run following commands as `python manage.py migrate` to do all the requried successful migrations. `python manage.py createsuperuser` to create a new super user for admin. To change the password run `python manage.py changepassword user_name`

### Models and Handling URL's
For media and image setting: Add `MEDIA_URL = '/media/' and MEDIA_ROOT = "[os.path.join(BASE_DIR, 'media')]"`. After doing any changes to data model, run `python manage.py makemigrations` and then, run `python manage.py migrate`.