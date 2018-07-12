import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "titan.settings")

import django

django.setup()

from django.db import transaction

from .models import Author


with transaction.automic():
    Author.objects.create(dd='sss')