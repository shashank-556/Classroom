from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import userSerializer

class userclass(APIView):
    "Register users"
    # user/
    # {'first_name','last_name','email','password'}
    def post(self,request):
        sr = userSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data,status=status.HTTP_201_CREATED)
        return Response(sr.errors,status=status.HTTP_400_BAD_REQUEST)
        
class userprofile(APIView):
    # user/<pk:int>/
    pass