# GeoserviceHUB

Hub for hosting of geospatial web services via OGC WPS.

## Dependenices

Django, PyWPS and others

```
pip install -r requirements.txt
```

## Setting up

```
django-admin startproject geoservicehub
git clone https://github.com/czechinvest/geoservicehub.git geoservicehub_lib
```

Now you have to adjust the `settings.py` file

1. Add `geoservicehub_lib` to `$PYTHONPATH`
2. Add geoservicehub apps to `INSTALLED_APPS`


In `settings.py`:

```
...
import sys
sys.path.append(os.path.join(BASEDIR, "../geoservicehub_lib/"))

...

INSTALLED_APPS = [
    'job.apps.JobConfig',
    'process.apps.ProcessConfig',
    ...
]

...

3. Point database to you PyWPS file/engine

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "/path/to/pywps-demo/logs/pywps-logs.sqlite3"
    }
}

```


Do further settings modifications.

## Init databse

```
python manage.py makemigrations
python manage.py migrate
```

## Testing

```
python manage.py runserver
```

And login as admin
