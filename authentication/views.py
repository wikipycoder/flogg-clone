from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistraterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from .models import User
from django.contrib.auth import authenticate, login, logout


class UserRegisterAPIView(APIView):

    def post(self, request):

        serializer = RegistraterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            try:
                token = Token.objects.get_or_create(user=user)[0]
            except Token.DoesNotFound:
                return Response(data="Token not created", status=HTTP_404_NOT_FOUND)
            print(token)
            response = {
                "email": user.email,
                "username": user.username,
                "token": token.key
            }

            return Response(response)

        return Response(serializer.errors)



class UserDoesNotExist(Exception):
    pass


class UserLoginAPIView(APIView):


    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = authenticate(username=username, password=password)

            if not user:
                raise UserDoesNotExist("User does not exist")

            token = Token.objects.get_or_create(user=user)[0]
        except UserDoesNotExist:
            return Response("User does not exist", status=HTTP_403_FORBIDDEN)
            
        except Token.DoesNotExist:
            return Response("Token Not Generated", status=HTTP_403_FORBIDDEN)
            
        
        if user.is_active:
            login(request, user)

        user_info = {"username": username, "token": token.key, "active": user.is_active, "request token": request.user.auth_token.key}
        return Response(user_info)



class UserLogoutAPIView(APIView):

    def get(self, request):             
        request.user.auth_token.delete()
        logout(request, request.user)


        

        