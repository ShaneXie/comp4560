from django.db import models

# Create your models here.
class Student(models.Model):
    old_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(blank=True, max_length=50)
    student_number = models.CharField(unique=True, max_length=20)

    stream = models.CharField(max_length=20)
    intake_session = models.CharField(max_length=20)
    intake_year = models.CharField(max_length=20)

    active = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    email = models.EmailField(max_length=128)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ',' + self.last_name
    #allow comment to be blank

class Company(models.Model):
    old_id = models.IntegerField(unique=True)
    active = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    
    status = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    government_type =  models.CharField(max_length=50)
    employerid = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    url = models.TextField(blank=True)
    company_name = models.TextField(blank=False)
    linda_comments = models.TextField(blank=True)
    gerri_comments = models.TextField(blank=True)
    last_contact = models.DateTimeField(blank=True)

    def __str__(self):
        return ','.join([self.company_name,self.city, '\n'+self.gerri_comments+'\n'])


class Term(models.Model):
    """docstring for Term"""
    old_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=80)  

    def __str__(self):
        return self.name      




class Posting(models.Model):
    """docstring fos Posting"""
    old_id = models.IntegerField(unique=True)
    hours_per_week = models.TextField(blank=True)
    number = models.IntegerField()
    remuneration = models.TextField(blank=True)
    file_name = models.TextField()
    comments = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    website = models.TextField(blank=True)
    coop_position = models.TextField()
    contact_position = models.TextField(blank=True)
    description = models.TextField(blank=True)
    street = models.TextField(blank=True)

    email = models.EmailField()
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dept = models.CharField(max_length=200, blank=True)
    #TODO these can be fk
    contact_last = models.CharField(max_length=50)
    contact_first = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)

    work_term = models.ForeignKey(Term)

class Placement(models.Model):
    old_id = models.IntegerField(unique=True)
    cetc_number = models.TextField(blank=True)
    student = models.ForeignKey(Student)
    posting = models.ForeignKey(Posting)
    remuneration = models.TextField(blank=True)


class Contact(models.Model):
    old_id = models.IntegerField()
    email = models.EmailField()
    province = models.CharField(max_length=50)
    position = models.TextField()
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dept = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    cell = models.CharField(max_length=50, blank=True)
    mail_method = models.CharField(max_length=30)
    contact_type = models.CharField(max_length=30)
    employer = models.ForeignKey(Company, null=True)
    
    complete = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    gerri_comments = models.TextField(blank=True)
    linda_comments = models.TextField(blank=True)
    address_1 = models.TextField(blank=True)
    address_2 = models.TextField(blank=True)
    
    def __str__(self):
        #employer = self.employer.company_name
        return ','.join([self.first_name,self.last_name,self.email])        



        