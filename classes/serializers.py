from rest_framework import serializers
from .models import room, content
from accounts.models import users

class roomSerializer(serializers.ModelSerializer) :
    creater = serializers.SerializerMethodField()

    def get_creater(self,cls:room):
        return cls.creater.get_full_name

    class Meta :
        model = room
        fields = ('id','name','description','created_at','creater')

class roomcreaterSerializer(serializers.ModelSerializer) :
    code = serializers.ReadOnlyField()

    class Meta :
        model = room
        fields = ('id','code','name','description','created_at')

class contentSerializer(serializers.ModelSerializer):
    class Meta :
        model = content
        fields = ('id','msg','created_at')


