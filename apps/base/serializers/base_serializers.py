from rest_framework import serializers


class UUIDFeildSerializer(serializers.Serializer):
    id = serializers.UUIDField()
