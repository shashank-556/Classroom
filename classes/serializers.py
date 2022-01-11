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
    fullname = serializers.SerializerMethodField('getname')

    def getname(self,mem:member):
        return mem.student.get_full_name()

    class Meta:
        model = member
        fields = ['fullname']
