from view_historical.models import Student, Company, Contact, Placement


def getStudentDT():
    students = Student.objects.all()
    return students


def getCompanyDT():
    companies = Company.objects.all()
    return companies


def getContactDT():
    contacts = Contact.objects.all()
    return contacts


def getPlacementDT():
    placement = Placement.objects.all()
    return placement