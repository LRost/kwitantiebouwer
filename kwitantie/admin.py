from django.contrib import admin
from .models import Kwitantie


class DefaultAdmin(admin.ModelAdmin):
    exclude = []


# Register your models here.
admin.site.register(Kwitantie, DefaultAdmin)

