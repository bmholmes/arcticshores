import sys, os, csv, json
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError
from candidates.models import Candidate, Score

class Command(BaseCommand):
    help = 'Imports and parses a JSON file and exports to csv.'

    def handle(self, *args, **options):
        json_file = os.path.join(sys.path[0], 'candidates.json')

        with open(json_file) as json_data:
            candidates = json.load(json_data)
            sorted_candidates = sorted(candidates, key=lambda candidate: candidate['score'])
        
        with open('candidates.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = candidates[0].keys())
            writer.writeheader()
            writer.writerows(sorted_candidates)