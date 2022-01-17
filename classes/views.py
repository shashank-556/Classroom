from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import room,content
from .serializers import roomSerializer,contentSerializer

not_found = {"detail": "not_found."}
not_authorised = {"detail":"not_authorised"}
not_allowed = {"detail":"not_allowed"}
not_part_of = {"detail":"not_part_of"}

class classinfo(APIView):
    """
    List name, description, creater of a classroom
    Endpoint: /class/<int:pk>/
    Methods allowed: (get)
    """
    
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
    Endpoint: /class/
    Methods Allowed: (post)
    Form Fields(post): {'name':'','description':''}
    """
    
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        
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
    Endpoint: /class/<int:pk>/content/
    Methods Allowed: (get,post)
    Form Fields(post): {'msg':''}
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        cls = get_object_or_404(room,pk=pk)
        return Response(data=contentSerializer(cls.contents.all(),many=True).data)


    def post(self,request,pk):
        
        cls = get_object_or_404(room,pk=pk)
        sr = contentSerializer(data = request.data)
        if sr.is_valid():
            sr.save(room=cls)
            return Response(sr.data,status=status.HTTP_201_CREATED)
        return Response(sr.errors,status.HTTP_400_BAD_REQUEST)

class content_ud(APIView):
    """
    Update or delete class content
    Endpoint: /class/<int:pk>/content/<int:pk>/
    Methods allowed: (put,delete)
    Form Fields(patch): {'msg':''}
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self,request,pk,pkc):
        cls = get_object_or_404(room,pk=pk)
        cnt = get_object_or_404(content,pk=pkc)
        if cnt in cls.contents.all():
            sr = contentSerializer(cnt,data=request.data)
            if sr.is_valid():
                sr.save()
                return Response(data=sr.data)
            else:
                return Response(data=sr.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=not_part_of,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,pkc):
        cls = get_object_or_404(room,pk=pk)
        cnt = get_object_or_404(content,pk=pkc)
        if cnt in cls.contents.all():
            cnt.delete()
            return Response(data=None,status=status.HTTP_200_OK)
        else:
            return Response(data=not_part_of,status=status.HTTP_400_BAD_REQUEST)



class class_members(APIView):
    """
    Display all the members of a class
    Endpoint: /class/<int:pk>/member/
    Methods allowed: (get)
    """
    # /class/<int:pk>/member/
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,pk):
        cls = get_object_or_404(room,pk=pk)
        
        
        return Response(data=None)
        


class join_class(APIView):
    """
    Join a classroom. Response 200(ok) is sent is user is already a part of classroom and 403(forbidden) if user is the creater
    of the classroom. Response 201(created) is sent upon successful joining of a class.
    Method allowed: (post)
    Endpoint: /class/join/
    Form Fields(post): {code:''}
    """  

    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        # {'code':''}

        cls = get_object_or_404(room,code=request.data['code'])

        if request.user == cls.creater:
            return Response(data=not_allowed,status=status.HTTP_403_FORBIDDEN)

        if request.user in cls.student.all():
            return Response(data=roomSerializer(cls).data,status=status.HTTP_200_OK)
        
        cls.student.add(request.user)
        return Response(data=roomSerializer(cls).data,status=status.HTTP_201_CREATED)    
