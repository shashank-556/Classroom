from rest_framework import serializers
from .models import users

class userSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 255,write_only=True,required = True,style={'input_type':'password'})
    class Meta :
        model = users
        fields = ('id','email','first_name','last_name','password','created_at')
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        user = users(email = validated_data['email'],
            last_name = validated_data['last_name'],
            first_name = validated_data['first_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user