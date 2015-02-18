from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from view_historical.models import Student
import sys
class Command(BaseCommand):
    help = 'import data from text file'
    
    def handle(self, *args, **options):
        """path for later use"""
        path = args[0]
        student_filter = ['userid','ipaddress','dateadded','datelastupdated',
            'sectionid', 'useridLastUpdated', 
            'adminEmailSent','stamp',
            'Comments_length','Comments_textIsHTML']
        self.port_table(student_filter, '/home/pykun/4560/dbs/student.txt')

    def port_table(self, columns_names, orgin):
        filter_out = map(lambda x:x.lower(), columns_names)
        intake_session = {'2':'december','3':'april','4':'summer'}
        intake_year = {unicode(x):unicode(1998+x) for x in xrange(2,17)}
        stream = {'2':'in stream','3':'out stream'}
        # exist_s=set()
        # exist_y=set()
        # exist_strea = set()
        with open(orgin, 'r') as r:
            lines = ''.join(r.readlines()).split('\t')
            lines =(x for x in lines[:-1])

            header = next(lines)
            new_schema = {index:value.lower() for index, value in enumerate(header.split('|')) 
                            if value.lower() not in filter_out}
            for row in lines:
                elements = map(lambda x:x.strip(), row.strip().split('|'))
                if len(elements[1]) < 14:
                    continue
                new_row = {'_'.join(new_schema[i].split(' ')):unicode(e, errors='ignore') for i,e in enumerate(elements) 
                            if i in new_schema.keys()}

                new_row['old_id'] = int(new_row['id'])
                del new_row['id']
                new_row['student_number'] = new_row['number']
                del new_row['number']

                new_row['complete'] = True if new_row['complete'] == 'True' else False
                new_row['active'] = True if new_row['active'] == 'True' else False
                new_row['intake_year'] = intake_year[new_row['intake_year']]
                new_row['intake_session'] = intake_session[new_row['intake_session']]
                new_row['stream'] =  stream[new_row['stream']]
                # exist_strea.add(new_row['stream'])
                # exist_y.add(new_row['intake_year'])
                # exist_s.add(new_row['intake_session'])
                #try:
                if len(Student.objects.filter(student_number=new_row['student_number']))>0:
                    #TODO log dup student numbers
                    continue
        # self.stdout.write(exist_s, ending='')
        # self.stdout.write('\n', ending='')
        # self.stdout.write(exist_y, ending='')
        # self.stdout.write('\n', ending='')
        # self.stdout.write(exist_strea, ending='')
        # self.stdout.write('\n', ending='')
                s = Student(**new_row)
                s.save()
