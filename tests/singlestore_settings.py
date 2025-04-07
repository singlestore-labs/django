# A settings file is just a Python module with module-level variables.

DJANGO_SETTINGS_MODULE = 'singlestore_settings'

DATABASES = {
    "default": {
        "ENGINE": "django_singlestore",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "",
        "NAME": "django_db",
    },
    "other": {
        "ENGINE": "django_singlestore",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "",
        "NAME": "django_db_other",
    },
}


USE_TZ = False
# TIME_ZONE = "UTC"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SECRET_KEY = 'your-unique-secret-key-here'
