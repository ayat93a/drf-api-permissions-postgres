from django.db import models
from django.contrib.auth import get_user_model


class Movie(models.Model):
    title = models.CharField(max_length= 100)
    actors = models.TextField(max_length= 250)
    imdb_rate = models.IntegerField(null= False)
    personal_review = models.TextField(null= True)
    reviwer = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)


    def __str__(self):
        return self.title
