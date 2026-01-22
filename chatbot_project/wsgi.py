"""
WSGI config for chatbot_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')

application = get_wsgi_application()

import os
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

try:
    if os.getenv("CREATE_SUPERUSER", "False") == "True":
        User = get_user_model()
        username = os.getenv("DJANGO_SU_NAME")
        email = os.getenv("DJANGO_SU_EMAIL")
        password = os.getenv("DJANGO_SU_PASSWORD")

        if username and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                print("✅ Superuser created successfully")
            else:
                print("✅ Superuser already exists")
except OperationalError:
    print("⚠️ Database not ready yet")
