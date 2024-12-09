from django.contrib import admin
from .models import AbstractClinicalEmployee, DRClinicalEmployee

# Register your models here.
admin.site.register(AbstractClinicalEmployee)
admin.site.register(DRClinicalEmployee)

