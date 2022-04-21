from django.contrib import admin
from .models import Branch,Zone,SubLocation,Field

# Register your models here.
admin.site.register(Branch)
admin.site.register(Zone)
admin.site.register(SubLocation)
admin.site.register(Field)