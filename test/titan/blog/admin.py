from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Title)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Author)
