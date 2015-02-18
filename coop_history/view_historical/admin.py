from django.contrib import admin
from view_historical.models import Student, Company, Contact

# Register your models here.

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Contact)
