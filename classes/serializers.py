from django.db.models import fields
from rest_framework import serializers
from .models import room, content
from accounts.serializers import userSerializer

class roomSerializer(serializers.ModelSerializer) :
    creater = serializers.SerializerMethodField()

    def get_creater(self,cls:room):
        return cls.creater.get_full_name()

    class Meta :
        model = room
        fields = ('id','name','description','created_at','creater')

class contentSerializer(serializers.ModelSerializer):
    class Meta :
        model = content
        fields = ('id','msg','created_at')

