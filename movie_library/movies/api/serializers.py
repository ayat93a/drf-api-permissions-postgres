from pyexpat import model
from attr import fields
from rest_framework import serializers
from movies.models import Movie

class Movieserializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movie