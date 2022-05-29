from pyexpat import model

from attr import fields
from nbformat import read
from .models import Singer,Song
from rest_framework import serializers

class SongSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    song=SongSerailizer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields=['id','name','gender','song']