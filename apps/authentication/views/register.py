# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# models imports
from apps.authentication.models import StudentMaster

# permissions
from rest_framework.permissions import AllowAny

# helper methods
from apps.helpers.model_helpers import getObjects

# serializers
from apps.authentication.serializers import StudentRegistrationSerializers

# password processors
from django.contrib.auth.hashers import make_password

# swager imports
from drf_spectacular.utils import extend_schema


class StudentRegisteration(APIView):
    # allowed permissions
    permission_classes = [AllowAny]

    # Swagger Schema for post api
    @extend_schema(
        request=StudentRegistrationSerializers,
    )
    def post(self, request, *args, **kwargs):
        """method to validate college email and to register students"""
        # serialize input data
        input_data = request.data
        student_data_serializers = StudentRegistrationSerializers(data=input_data)

        # handle incomplete and invalid inputs
        if not student_data_serializers.is_valid():
            return Response({"error": student_data_serializers.errors}, status=400)

        # prepocessing
        input_email = input_data.get("email", None)
        password = input_data.get("password")

        # check the uniqueness of email
        student_obj = StudentMaster.objects.filter(email=input_email).first()
        if student_obj is not None:
            return Response({"error": "entered email already exists!"}, status=400)

        # check provided email is valid college email or not
        email = input_email.split("@")
        if email[1] == "gmail.com":
            return Response(
                {"error": "please provide college email, gmail.com not allowed!"},
                status=400,
            )

        # update the email in serializers data
        input_data["email"] = input_email

        # hashed_password
        hashed_password = make_password(password)

        # hash the password
        final_data = {**input_data, "password": hashed_password}

        # save the data
        student_data = StudentRegistrationSerializers(data=final_data)

        if not student_data.is_valid():
            return Response({"error": student_data.errors}, status=400)
        student_data.save()

        return Response({"message": "ohoo! student registered"}, status=201)
