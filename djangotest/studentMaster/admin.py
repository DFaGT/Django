from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import dbtest

from .models import Student

from .models import Parent

from .models import School

admin.site.register(dbtest)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(School)