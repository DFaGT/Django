from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import dbtest

from .models import student

from .models import parent

admin.site.register(dbtest)
admin.site.register(student)
admin.site.register(parent)