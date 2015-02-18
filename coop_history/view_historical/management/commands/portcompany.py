from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from view_historical.models import Company
import sys
import datetime

class Command(BaseCommand):
    help = 'import data from text file'
    
    def handle(self, *args, **options):
        """path for later use"""
        path = args[0]
        company_filter = ['stamp','ipaddress','adminEmailSent','useridLastUpdated',
            'Gerri Comments_length','Linda Comments_length','Linda Comments_textIsHTML',
            'Gerri Comments_textIsHTML','userid','sectionid','dateadded', 'datelastupdated']
        self.port_table(company_filter, '/home/pykun/4560/dbs/company.txt')

    def port_table(self, columns_names, orgin):
        filter_out = map(lambda x:x.lower(), columns_names)

        status_dict={'2':'active','3':'not active','4':'no further contact required'}
        government_dict = {'0':'not','2':'Federal', '3':'Provincial', '4':'municipal'}
        status = {'2':'active','3':'not active','4':'no further contact required'}

        type_dict = {} 

        with open(orgin, 'r') as r:
            lines = ''.join(r.readlines()).split('\t')
            lines =(x for x in lines[:-1])

            header = next(lines)
            new_schema = {index:value.lower() for index, value in enumerate(header.split('|')) 
                            if value.lower() not in filter_out}
            #self.stdout.write(new_schema, ending='')
            #sys.exit()
            for row in lines:
                elements = map(lambda x:x.strip(), row.strip().split('|'))
                if len(elements[1]) < 14:
                    continue
                new_row = {'_'.join(new_schema[i].split(' ')):unicode(e, errors='ignore') 
                                for i,e in enumerate(elements) if i in new_schema.keys()}

                new_row['old_id'] = int(new_row['id'])
                new_row['active'] = True if new_row['active'] == 'True' else False
                new_row['complete'] = True if new_row['complete'] == 'True' else False

                new_row['government_type'] = government_dict[new_row['government'].strip()]
                del new_row['government']
                new_row['company_name'] = new_row['employer']
                del new_row['employer']
                new_row['status'] = status_dict[new_row['status']]
                (time_str,_) = new_row['last_contact'].split(' ')
                new_row['last_contact'] = datetime.datetime.strptime(time_str, "%Y-%m-%d")
                #new_row['']
                #self.stdout.write(timestr, ending='')
                #break
                #try:
                #if len(Student.objects.filter(student_number=new_row['student_number']))>0:
                    #TODO log dup student numbers
                #   continue
                #self.stdout.write(new_row, ending='')
                c = Company(**new_row)
                # for k,x in new_row.items():
                #     if x.__class__ == unicode('a').__class__:
                #         self.stdout.write(k+':'+str(len(x)),ending='')
                #         self.stdout.write('\n',ending='')

                #self.stdout.write(c, ending='')
                #try:
                #break
                c.save()
                #except:
                #    self.stdout.write(c,ending='')
                #    sys.exit()
