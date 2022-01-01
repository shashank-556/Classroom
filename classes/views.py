from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import info,content
from .serializers import infoSerializer,contentSerializer

not_found = {"detail": "Not found."}

class classinfo(APIView):
    """
    List name, description, creater of a classroom
    """
    # class/<int:pk>
    permission_classes = [permissions.IsAuthenticated]    
    def get(self,request,pk):

        cls = get_object_or_404(info,pk= pk)
        sr = infoSerializer(cls)
        return Response(sr.data,status = status.HTTP_200_OK)

    
class create_class(APIView):
    """
    Create class
    """
    # class/
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        # {'name':'','description':'',creater_id:''}
        sr = infoSerializer(data = request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data,status=status.HTTP_201_CREATED)
        return Response(sr.errors,status = status.HTTP_400_BAD_REQUEST)

class class_content(APIView):
    """
    Create and display content of a class
    """
    # class/<int:pk>/content

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk):
        if info.objects.filter(pk = pk).exists():
            cnt = content.objects.filter(classid=pk)
            sr = contentSerializer(cnt,many=True)
            return Response(sr.data)
        else :
            return Response(not_found,status = status.HTTP_404_NOT_FOUND)


    def post(self,request,pk):
        # {'msg':''}
        if info.objects.filter(pk=pk).exists():
            dt = request.data.copy()
            dt['classid'] = pk
            sr = contentSerializer(data = dt)
            if sr.is_valid():
                sr.save()
                return Response(sr.data,status=status.HTTP_201_CREATED)
            return Response(sr.errors,status.HTTP_400_BAD_REQUEST)
        else:
            return Response(not_found,status = status.HTTP_404_NOT_FOUND)


    

    
