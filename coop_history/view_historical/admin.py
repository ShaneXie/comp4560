from django.contrib import admin
from view_historical.models import Student, Company, Contact, Term, Posting,Placement

# Register your models here.

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Term)
admin.site.register(Posting)
admin.site.register(Placement)