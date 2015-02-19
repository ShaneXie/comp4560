from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from view_historical.models import Term,Posting
import sys
class Command(BaseCommand):
    help = 'import data from text file'
    
    def handle(self, *args, **options):
        """path for later use"""
        path = args[0]
        posting_filter = ['stamp',
        'userId','dateAdded',
        'userIdLastUpdated','dateLastUpdated',
        'active','adminEmailSent','Companyx',
        'complete','ipAddress','Comments_textIsHTML',
        'Comments_length','Qualifications_textIsHTML',
        'Qualifications_length','Description_textIsHTML',
        'Description_length','Job poster_documentId',
        'Job poster_fileSize','sectionId']

        self.port_table(posting_filter, '/home/pykun/4560/dbs/posting.txt')

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
                new_row['province'] = int(new_row['province_1'])
                del new_row['province_1']
                #new_row['hours_per_week'] = float(new_row['hours_per_week'])
                new_row['contact_position'] = new_row['position']
                del new_row['position']
                new_row['phone'] = new_row['telephone']
                del new_row['telephone']
                new_row['fax'] = new_row['fax_number']
                del new_row['fax_number']
                new_row['file_name'] = new_row['job_poster_filename']
                del new_row['job_poster_filename']

                new_row['number'] = int(new_row['number'])
                t = Term.objects.filter(old_id = int(new_row['work_term']))[0]
                new_row['work_term'] = t
                # if 'remuneration' in new_row:
                #     if len(new_row['remuneration'])>0:
                #     # self.stdout.write(len(new_row['remuneration']),ending='')
                #     # self.stdout.write('\n',ending='')
                #         new_row['remuneration'] = float(new_row['remuneration'])
                #     else:
                #         new_row['remuneration'] = 0

                # if 'hours_per_week' in new_row:
                #     if len(new_row['hours_per_week'])>0:
                #     # self.stdout.write(len(new_row['remuneration']),ending='')
                #     # self.stdout.write('\n',ending='')
                #         new_row['hours_per_week'] = float(new_row['hours_per_week'])
                #     else:
                #         new_row['hours_per_week'] = 0
                p = Posting(**new_row)
                p.save()
