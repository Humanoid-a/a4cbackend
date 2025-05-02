from django.core.management import call_command
from django.conf import settings
import os

# ensure settings are loaded
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "a4cbackend.settings")
import django
django.setup()

# then:
call_command("makemigrations", verbosity=2)
call_command("migrate", verbosity=2)
