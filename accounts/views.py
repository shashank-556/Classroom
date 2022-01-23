from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import userSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class userclass(APIView):
    """
    Register Users
    Endpoint: /register/
    Methods Allowed: (post)
    Form Fields(post): {'first_name','last_name','email','password'}
    """

    def post(self,request):
        sr = userSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data,status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)

 # for custom claims in token       
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_name'] = user.get_full_name

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer