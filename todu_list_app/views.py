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