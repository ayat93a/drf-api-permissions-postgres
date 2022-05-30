from rest_framework import serializers
from movies.models import Movie

class Movieserializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [ 'id' , 'title' , 'actors' , 'imdb_rate' , 'personal_review' , 'reviwer']
    