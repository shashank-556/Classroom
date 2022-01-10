from django.db.models import fields
from rest_framework import serializers
from .models import room, content, member

class roomSerializer(serializers.ModelSerializer) :
    class Meta :
        model = room
        fields = ['id','name','description','created_at']

class contentSerializer(serializers.ModelSerializer):
    class Meta :
        model = content
        fields = '__all__'

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = member
        fields = '__all__'
