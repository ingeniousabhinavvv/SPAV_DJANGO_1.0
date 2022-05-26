from django.contrib import admin
from .models import carousel, flashNews, GoiInitiative, Studentworks, Faculty, Noticeboard

# Register your models here.
admin.site.register(Faculty)
admin.site.register(carousel)
admin.site.register(flashNews)
admin.site.register(GoiInitiative)
admin.site.register(Studentworks)
admin.site.register(Noticeboard)
