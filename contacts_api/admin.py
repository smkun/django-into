from django.contrib import admin

# Register your models here.
from .models import Company, Contact
admin.site.register(Company)
admin.site.register(Contact)