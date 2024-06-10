from django.db import models
# Create your models here.
from musician.models import Musician

class Album(models.Model):
    CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    
    album_name = models.CharField(max_length=50)
    album_release_date= models.DateField()
    rating= models.CharField(max_length=20, choices=CHOICES)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.album_name