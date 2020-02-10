from django.contrib import admin

# Register your models here.
from .models import Candidate, Score

admin.site.register(Candidate)
admin.site.register(Score)