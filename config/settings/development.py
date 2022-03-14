from config.settings.base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("POSTGRES_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": os.environ.get("POSTGRES_NAME", default="db_sqllite3"),
        "USER": os.environ.get("POSTGRES_USER", default="postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", default="postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", default="postgres"),
        "PORT": os.environ.get("POSTGRES_PORT", default=5432),
    },
    "mongo": {
        "name": os.environ.get("MONGO_NAME", default="test_mongo"),
        "host": os.environ.get("MONGO_HOST", default="mongodb://mongodb:27017/"),
        "tz_aware": True,
    },
}
