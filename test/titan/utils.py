import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "titan.settings")

import django

django.setup()

from django.db import transaction

from blog.models import Author


try:
    with transaction.atomic():
        Author.objects.create(name='ddd')
        Author.objects.create(dd='sss')
except:
    pass