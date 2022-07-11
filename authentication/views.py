from django.contrib import auth
from .serializers import UserSerializer, LoginSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
import jwt
from django.conf import settings


class RegisterView(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        auth_data = request.data
        username = auth_data.get('username', '')
        password = auth_data.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth_token = jwt.encode({'username': user.username},
                                    settings.JWT_SECRET_KEY, algorithm="HS256"
                                    )
            serializer = UserSerializer(user)
            data = {
                "user": serializer.data,
                "token": auth_token
            }

            return Response(data, status=status.HTTP_200_OK)
        return Response({"Details": "Invalid credentials"})
