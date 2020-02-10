from django.forms import ModelForm
from .models import Candidate, Score

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = [
            "name",
            "candidate_ref",
        ]

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = [
            'candidate',
            'score',
        ]