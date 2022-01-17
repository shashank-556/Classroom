from rest_framework import serializers
from .models import room, content
from accounts.models import users

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

class memberSerializer(serializers.ModelSerializer) :
    full_name = serializers.CharField(source='get_full_name')

    class Meta :
        model = users
        fields = ('full_name',)
