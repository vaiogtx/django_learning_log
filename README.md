# django_learning_log
Django project from book "Python Crash Code, 3rd Ed."

## Setup the virtual environment

### Create venv and activate the venv

Create a new virtual environment named *ll_env* and activate it.
```powershell
python -m venv ll_venv
./llvenv/Scripts/activate.ps1
```

With the venv activated, update pip and install django
```powershell
pip install --upgrade pip
pip install django
```

## Create a new Django project

Create a project called *ll_project*
```powershell
django-admin startproject ll_project . # with the ".", created in current directory
```

Create the database with ```makemigrations``` and ```migrate```
```powershell
python manage.py makemigrations 
python manage.py migrate
```

View the project
```powershell
python manage.py runserver
```

## Start a new App

Create a new app called *learning_logs*
```powershell
python manage.py start app learning_logs
```

Add models in *models.py*, after the models is added, remember to ```makemigrations``` and ```migrate```
```powershell
python manage.py makemigrations learning_logs
python manage.py migrate
```
The table will be created after running ```migrate```

### Register the new app to the project

In ```settings.py```, add the app into the ```INSTALLED_APP```
```python
INSTALLED_APPS = [
	'learning_logs',
]
```

## Setting Up a Superuser

Create a superuser with ```createsuperuser```
```powershell
pyhon manage.py createsuperuser
```

## Registering a Model with the Admin Site

Register the models in the *admin.py* in the app folder
```python
from .models import Topic

admin.site.register(Topic)
```

## The Django Shell

Using the Django Shell for testing and trouble-shooting
```powershell
python manage.py shell
```

Query the data
```python
from learning_logs.modles import Topic
topics = Topic.objects.all()
for topic in topics:
	print(topic.id, topic)
```
