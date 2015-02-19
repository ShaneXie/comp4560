from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from view_historical.models import Student, Posting, Placement
import sys
class Command(BaseCommand):
    help = 'import data from text file'
    
    def handle(self, *args, **options):
        """path for later use"""
        path = args[0]
        term_filter = ['userid','ipaddress','dateadded',
        'datelastupdated','sectionid', 'active','complete',
        'adminEmailSent','stamp','useridlastupdated']
        self.port_table(term_filter, '/home/pykun/4560/dbs/placement.txt')

    def port_table(self, columns_names, orgin):
        filter_out = map(lambda x:x.lower(), columns_names)
        #self.stdout.write(filter_out,ending='')
        with open(orgin, 'r') as r:
            lines = ''.join(r.readlines()).split('\t')
            lines =(x for x in lines[:-1])

            header = next(lines)
            new_schema = {index:value.lower() for index, value in enumerate(header.split('|')) 
                            if value.lower() not in filter_out}
            #self.stdout.write(new_schema,ending='')
            for row in lines:
                elements = map(lambda x:x.strip(), row.strip().split('|'))
                if len(elements[1]) < 14:
                    continue
                new_row = {'_'.join(new_schema[i].split(' ')):unicode(e, errors='ignore') for i,e in enumerate(elements) 
                            if i in new_schema.keys()}

                new_row['old_id'] = int(new_row['id'])
                del new_row['id']
                qs = Student.objects.filter(old_id=int(new_row['student']))
                if len(qs) == 0:
                    continue
                    self.stdout.write(new_row,ending='')
                    sys.exit()
                new_row['student'] = qs[0]
                qp = Posting.objects.filter(old_id=int(new_row['posting']))
                if len(qp) == 0:
                    continue
                    self.stdout.write(new_row,ending='')
                    sys.exit()
                new_row['posting'] = qp[0]

                pl = Placement(**new_row)
                pl.save()
