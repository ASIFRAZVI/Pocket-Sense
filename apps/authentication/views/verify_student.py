# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# models imports
from apps.authentication.models import StudentMaster, OtpMaster

# permissions
from rest_framework.permissions import AllowAny

# helper methods
from apps.helpers.model_helpers import getObjects

# serializers
from apps.authentication.serializers import OtpSerializers

# swager imports
from drf_spectacular.utils import extend_schema

# timezone imports
from django.utils import timezone
from datetime import timedelta

# helper methods
from apps.helpers.random_otp_generator import generate_random_otp


class VerifyStudent(APIView):
    # allowed permissions
    permission_classes = [AllowAny]

    # Swagger Schema for post api
    @extend_schema(
        request=OtpSerializers,
    )
    def post(self, request, *args, **kwargs):
        # get the request data
        input_data = request.data

        input_otp = input_data.get("otp", None)
        input_email = input_data.get("email", None)

        # filter student object from database
        student_obj = StudentMaster.objects.filter(email=input_email).first()

        if student_obj is None:
            return Response({"error": "student not found with this email"}, status=400)

        # time limit for OTP validit
        valid_time_limit = timezone.now() - timedelta(minutes=10)

        # filter otp object from database
        otp_obj = OtpMaster.objects.filter(
            user=student_obj.id,
            otp=input_otp,
            is_used=False,
            created__gte=valid_time_limit,
        ).first()

        if otp_obj is None:
            return Response({"error": "Invalid OTP or OTP has expired"}, status=400)

        # make otp as used
        otp_obj.is_used = True
        student_obj.is_active = True
        student_obj.save()
        otp_obj.save()

        return Response({"message": "OTP verified successfully"}, status=200)


@api_view(["POST"])
def resend_otp(request, *args, **kwargs):
    # request data
    input_data = request.data
    input_email = input_data.get("email", None)

    # filter student
    student_obj = StudentMaster.objects.filter(email=input_email).first()

    if student_obj is None:
        return Response({"error": "student not found with this email"}, status=400)

    # generate new-otp
    otp = generate_random_otp(length=6)

    # save otp to database
    otp_obj = OtpMaster(user=student_obj, otp=otp)
    otp_obj.save()

    # after creation singnal will send email to student with otp
    return Response({"message": "OTP resent successfully"}, status=200)
