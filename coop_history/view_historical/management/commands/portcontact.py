from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from view_historical.models import Contact,Company
import sys
class Command(BaseCommand):
    help = 'import data from text file'
    
    def handle(self, *args, **options):
        """path for later use"""
        path = args[0]
        contact_filter = ['sectionid', 'userid',
        'dateAdded','userIdLastUpdated',
        'Linda Comments_textIsHTML',
        'Linda Comments_length',
        'dateLastUpdated','ipaddress',
        'adminEmailSent','Gerri Comment',
        'Gerri Comment_textIsHTML',
        'Gerri Comment_length',
        'stamp']
        self.port_table(contact_filter, '/home/pykun/4560/dbs/contact.txt')

    def port_table(self, columns_names, orgin):
        filter_out = map(lambda x:x.lower(), columns_names)

        type_dict = {'0':'NA','2':'primary','3':'second','4':'former'}
        mail_method = {'0':'NA0','1':'NA','2':'post','3':'email','4':'do not email'}

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
                c_list = Company.objects.filter(old_id=int(new_row['employer_id']))
                if len(c_list) > 0:
                    new_row['employer'] = c_list[0]
                else:
                    self.stdout.write(new_row['employer_id'],ending='')
                    self.stdout.write('\n',ending='')
                del new_row['employer_id']
                
                new_row['active'] = True if new_row['active'] == 'True' else False
                new_row['complete'] = True if new_row['complete'] == 'True' else False
                
                new_row['mail_method'] = mail_method[new_row['mail_method']]
                new_row['contact_type'] = type_dict[new_row['type']]
                del new_row['type']
                c = Contact(**new_row)
                #try:
                c.save()
                # except Exception,e:
                #     for i,v in new_row.items():
                #         if v.__class__ == unicode('a').__class__:
                #             print i,len(v)
                #     sys.exit()
