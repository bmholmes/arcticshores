import sys, os, csv, json
from .models import Candidate, Score
from django.core.exceptions import ValidationError

def import_csv():
    csv_file = os.path.join(sys.path[0], 'candidates.csv')

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
                s = _.score_set.create(score=row[2])
            except ValidationError as err:
                print('; '.join(err.messages))
                next

def import_json():
    json_file = os.path.join(sys.path[0], 'candidates.json')

    with open(json_file) as json_data:
        candidates = json.load(json_data)
        sorted_candidates = sorted(candidates, key=lambda candidate: candidate['score'])
    
    with open('candidates.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = candidates[0].keys())
        writer.writeheader()
        writer.writerows(sorted_candidates)