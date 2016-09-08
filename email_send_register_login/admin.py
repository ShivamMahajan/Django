from django.contrib import admin

# Register your models here.

from .forms import insert ,Email

admin.site.register(insert)
admin.site.register(Email)