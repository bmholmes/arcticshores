from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(
        max_length=200
    )
    candidate_ref = models.CharField(
        primary_key=True, 
        unique=True, 
        max_length=8, 
        validators=[RegexValidator(
            regex='^\w{8}$', 
            message='Candidate Reference must be 8 alphanumeric characters.', 
            code='invalid'
        )]
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Candidate, self).save(*args, **kwargs)

class Score(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        related_name='scores',
        on_delete=models.CASCADE
    )
    score = models.FloatField(
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(100)
        ]
    )

    class Meta:
        ordering = ['score']

    def __str__(self):
        return str(self.score)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Score, self).save(*args, **kwargs)