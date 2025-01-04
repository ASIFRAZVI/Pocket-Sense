from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from apps.helpers.jwt_decoder import decode_jwt_token


class StudentLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [decode_jwt_token]

    def post(self, request, *args, **kwargs):
        """Logout by clearing cookies"""

        # res
        response = Response(
            {"message": "Logout successful."},
            status=200,
        )

        # Delete both tokens
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response
