from view_historical.models import Student


def getStudentDT():
    students = Student.objects.all()
    return students