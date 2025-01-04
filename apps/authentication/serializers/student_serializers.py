from rest_framework import serializers
from apps.authentication.models import StudentMaster, OtpMaster


class StudentRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentMaster
        exclude = ["id", "is_active", "last_login"]


class StudentLoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)


class OtpSerializers(serializers.Serializer):
    otp = serializers.IntegerField()
    email = serializers.EmailField()
