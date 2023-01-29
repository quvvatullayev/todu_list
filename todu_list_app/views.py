from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serialization import(
    UserSerializer,
    ToduSerializer
)
from .models import User, Todu

# Create your views here.

class UserView(APIView):
    def post(self, request:Request):
        data_usre = request.data
        user = UserSerializer(data=data_usre, many = False)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors)

    def get(self, request:Request, pk):
        user_filter = User.objects.get(id = pk)
        user = UserSerializer(user_filter, many = False)
        return Response(user.data)

class UserUpdate(APIView):
    def post(self,request:Request, pk):
        user_filter = User.objects.get(id = pk)
        data = request.data
        user_filter.username = data.get("username", user_filter.username)
        user_filter.email = data.get("email", user_filter.email)
        user_filter.password = data.get("password", user_filter.password)
        user_filter.save()
        user = UserSerializer(user_filter, many = False)
        return Response(user.data)

class DeleteUser(APIView):
    def get(self, request:Request, pk):
        user_filter = User.objects.get(id = pk)
        user_filter.delete()
        return Response({'Delete user': 'Ok'})