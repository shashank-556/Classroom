from rest_framework import serializers
from .models import info, content

class infoSerializer(serializers.ModelSerializer) :
    class Meta :
        model = info
        fields = '__all__'

class contentSerializer(serializers.ModelSerializer):
    class Meta :
        model = content
        fields = '__all__'