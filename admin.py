from django.contrib import admin

from .models import *

class SomeModelAdmin(admin.ModelAdmin)
    pass

# admin.site.register(SomeModel, SomeModelAdmin)