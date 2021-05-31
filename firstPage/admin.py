from django.contrib import admin
from django.http import request, response
import requests

# Register your models here.

from firstPage.models import Person, Course, Grade


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # requests.get("http://localhost:8000/add_person_notify/")
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass
