import email
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.response import Response
from rest_framework import status

class UserAPI(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data = {
            "email":request.data.get('email'),
            "first_name":request.data.get('first_name'),
            "last_name":request.data.get('last_name'),
            "password":request.data.get('password')
        }
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            user = User.objects.create(
                email = data['email'],
                first_name = data['first_name'],
                last_name = data['last_name']
            )
            if user:
                user.set_password(data['password'])
                user.save()
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




