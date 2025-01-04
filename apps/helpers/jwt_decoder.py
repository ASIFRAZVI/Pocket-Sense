import jwt
from pathlib import os
from rest_framework import authentication
from rest_framework import exceptions
from apps.authentication.models import StudentMaster
from django.conf import settings

# Existing authentication logic...

# JWT_SECRET=os.getenv('JWT_SECRET')
# def decode_jwt_token(request, JWT_SECRET):
#     """normal custom Jwt decoder"""
#     jwt_token = request.COOKIES.get('access_token')

#     try:
#         payload = jwt.decode(jwt_token, JWT_SECRET, algorithms=['HS256'])
#         return payload

#     except jwt.ExpiredSignatureError:
#         raise Exception("JWT token has expired")
#     except jwt.InvalidTokenError:
#         raise Exception("Invalid JWT token")


# overriding the DRF Auth
class decode_jwt_token(authentication.BaseAuthentication):
    def authenticate(self, request):
        JWT_SECRET = settings.JWT_SECRET
        jwt_token = request.COOKIES.get("access_token")

        if not jwt_token:
            return None

        try:
            payload = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])
            user_id = payload.get("user_id")

            user = StudentMaster.objects.filter(id=user_id).first()
            if not user:
                raise exceptions.AuthenticationFailed("User not found")

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("JWT token has expired")
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed("Invalid token")
        except StudentMaster.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found")

        return (user, None)
