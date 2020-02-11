import sys, os, csv
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from candidates.models import Candidate, Score

class Command(BaseCommand):
    help = 'Imports values from csv file and adds valid entries to database.'

    def handle(self, *args, **options):
        try:
            csv_file = os.path.join(sys.path[0], input('Enter csv file name:'))   
            with open(csv_file, newline='') as candidates:
                has_header = csv.Sniffer().has_header(candidates.read(1024))
                candidates.seek(0)
                file = csv.reader(candidates, delimiter=',')
                if has_header:
                    next(file)
                for row in file:
                    try:
                        _, created = Candidate.objects.get_or_create(
                            candidate_ref=row[0],
                            name=row[1],
                        )
                        _.scores.create(score=row[2])
                        if created:
                            print('Candidate %s created' % _.name)
                        else:
                            print('Candidate %s updated' % _.name)
                    except ValidationError as err:
                        print('Error: ','; '.join(err.messages))
                        next
        except FileNotFoundError as err:
            print(err)
        except:
            print('Please enter a valid .csv file')