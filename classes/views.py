from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import users
from .models import room,content, member
from .serializers import roomSerializer,contentSerializer

not_found = {"detail": "not_found."}
not_authorised = {"detail":"not_authorised"}

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
            sr.save(code = room.generate_code(),creater=request.user)
            return Response(sr.data,status=status.HTTP_201_CREATED)
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
    # /class/<int:pk>/members
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        mem = member.objects.filter(class_id = pk)
        b = False
        di = []
        if request.user == room.objects.get(pk = pk).creater:
            b = True

        for i in mem:
            usr = users.objects.get(i.user_id)
            if request.user == usr:
                b = True
            di.append(usr.get_full_name())
        if b:
            return Response(di,status=status.HTTP_200_OK)
        return Response(not_authorised,status=status.HTTP_403_FORBIDDEN)

    def post(self,request,pk):
        m = member(user_id = request.user.id,class_id = pk)
        m.save()
        request(status=status.HTTP_201_CREATED)    

    
