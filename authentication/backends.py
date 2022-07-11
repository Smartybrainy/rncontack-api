from rest_framework import authentication
import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import exceptions


class JWTAuthenticaion(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split(" ")

        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET_KEY, algorithms="HS256")

            user = User.objects.get(username=payload['username'])
            return (user, token)

        except jwt.DecodeError as identifier:
            exceptions.AuthenticationFailed("Your token is invalid!")
        except jwt.ExpiredSignatureError:
            exceptions.AuthenticationFailed("Your token has expired.")
