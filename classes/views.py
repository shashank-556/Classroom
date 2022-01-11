from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import users
from .models import room,content, member
from .serializers import roomSerializer,contentSerializer,memberSerializer

not_found = {"detail": "not_found."}
not_authorised = {"detail":"not_authorised"}
not_allowed = {"detail":"not_allowed"}

class classinfo(APIView):
    """
    List name, description, creater of a classroom
    """
    # class/<int:pk>
    permission_classes = [permissions.IsAuthenticated]    
    def get(self,request,pk):

        cls = get_object_or_404(room,pk= pk)
        sr = roomSerializer(cls)
        
        if cls.creater == request.user:
            temp = {'code':cls.code}
            temp.update(sr.data)
            return Response(temp,status = status.HTTP_200_OK)

        return Response(sr.data,status = status.HTTP_200_OK)

    
class create_class(APIView):
    """
    Create class
    """
    # class/
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        # {'name':'','description':'',creater_id:''}
        sr = roomSerializer(data = request.data)
        if sr.is_valid():
            cls = sr.save(code = room.generate_code(),creater=request.user)
            temp = {'code':cls.code}
            temp.update(sr.data)
            return Response(temp,status = status.HTTP_201_CREATED)
        return Response(sr.errors,status = status.HTTP_400_BAD_REQUEST)

class class_content(APIView):
    """
    Create and display content of a class
    """
    # class/<int:pk>/content

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        if room.objects.filter(pk = pk).exists():
            cnt = content.objects.filter(classid=pk)
            sr = contentSerializer(cnt,many=True)
            return Response(sr.data)
        else :
            return Response(not_found,status = status.HTTP_404_NOT_FOUND)


    def post(self,request,pk):
        # {'msg':''}
        if room.objects.filter(pk=pk).exists():
            dt = request.data.copy()
            dt['classid'] = pk
            sr = contentSerializer(data = dt)
            if sr.is_valid():
                sr.save()
                return Response(sr.data,status=status.HTTP_201_CREATED)
            return Response(sr.errors,status.HTTP_400_BAD_REQUEST)
        else:
            return Response(not_found,status = status.HTTP_404_NOT_FOUND)

class class_members(APIView):
    """
    Display all the members of a class
    """
    # /class/<int:pk>/member
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        mem = member.objects.filter(room_id = pk)
        
        return Response(data=memberSerializer(mem,many=True).data)
        


class join_class(APIView):
    
    # /class/join/

    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        # {'code':''}
        code = request.data['code']
        cls = get_object_or_404(room,code=code)

        if request.user == cls.creater:
            return Response(data=not_allowed,status=status.HTTP_403_FORBIDDEN)

        if member.objects.filter(student=request.user,room=cls).exists():
            return Response(data=roomSerializer(cls).data,status=status.HTTP_200_OK)
        
        temp = member(student = request.user,room=cls)  
        temp.save()
        return Response(data=roomSerializer(cls).data,status=status.HTTP_201_CREATED)    
