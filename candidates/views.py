from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
from .models import Candidate, Score

def index(request):
    candidate_score_list = Candidate.objects.order_by('name')
    highest_score = Score.objects.aggregate(Max('score'))
    
    context = {'candidate_score_list': candidate_score_list, 'highest_score': highest_score}
    return render(request, 'candidates/index.html', context)
