# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from django.db.models import Sum

# models imports
from apps.authentication.models import StudentMaster
from apps.expense_tracker.models import ExpenseMaster

# permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

# helper methods
from apps.helpers.model_helpers import getObjects

# serializers
from apps.expense_tracker.serializers import ExpenseMasterSerializer
from apps.base.serializers import UUIDFeildSerializer

# swager imports
from drf_spectacular.utils import extend_schema

# authentications
from apps.helpers.jwt_decoder import decode_jwt_token


class ExpenseView(APIView):
    # allowed permissions
    permission_classes = [IsAuthenticated]
    # authentication_classes = [decode_jwt_token]

    # Swagger Schema for post api
    @extend_schema(
        request=ExpenseMasterSerializer,
    )
    def post(self, request, *args, **kwargs):
        """method to add a new expense"""
        # input data
        input_data = request.data

        # get user id from jwt token
        user_id = request.user.id

        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        student_obj = StudentMaster.objects.filter(id=validated_user_id).first()
        if student_obj is None:
            return Response({"error": "Student not found"}, status=400)

        input_data["student"] = student_obj.id
        expense_data_serializers = ExpenseMasterSerializer(data=input_data)

        # handle incomplete and invalid inputs
        if not expense_data_serializers.is_valid():
            return Response({"error": expense_data_serializers.errors}, status=400)

        expense_data_serializers.save()

        # final_data = {"student": student_obj, **input_data}

        # # create new expense
        # expense_obj = ExpenseMaster.objects.create(**final_data)
        return Response({"message": "expense added"}, status=201)

    def get(self, request, expense_id=None, catogary=None, *args, **kwargs):
        """method to get all expenses or specific expense"""
        # get user id from jwt token
        user_id = request.user.id

        # check uuid
        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        student_obj = StudentMaster.objects.filter(id=validated_user_id).first()
        if student_obj is None:
            return Response({"error": "Student not found"}, status=400)

        # get all expenses
        if expense_id is None and catogary is None:
            expense_objects = ExpenseMaster.objects.filter(student=student_obj)
            serializer = ExpenseMasterSerializer(expense_objects, many=True)
            return Response(serializer.data, status=200)

        # get specific expense
        elif expense_id and catogary is None:
            expense_obj = ExpenseMaster.objects.filter(
                student=student_obj, id=expense_id
            ).first()
            if expense_obj is None:
                return Response({"error": "Expense not found"}, status=404)

            expense_serializer = ExpenseMasterSerializer(expense_obj)
            return Response(expense_serializer.data, status=200)

        # get expenses by catogary
        input_catogary = request.GET.get("catogary", None)
        processed_catogary = input_catogary.lower().replace(" ", "_")
        expense_objs = ExpenseMaster.objects.filter(
            student=student_obj, expense_catogary=processed_catogary
        ).first()
        if expense_objs is None:
            return Response(
                {"error": "Expense not found for provided catogary"}, status=404
            )

        catogary_serializer = ExpenseMasterSerializer(expense_objs, many=True)
        return Response(catogary_serializer.data, status=200)

    def patch(self, request, expense_id=None, *args, **kwargs):
        """method to update specific expense"""

        if expense_id is None:
            return Response({"error": "Expense id is required"}, status=400)

        # serialize input data
        input_data = request.data

        # get user id from jwt token
        user_id = request.user.id

        # check uuid
        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        student_obj = StudentMaster.objects.filter(id=validated_user_id).first()
        if student_obj is None:
            return Response({"error": "Student not found"}, status=400)

        # get specific expense
        expense_obj = ExpenseMaster.objects.filter(
            student=student_obj, id=expense_id
        ).first()
        if expense_obj is None:
            return Response({"error": "Expense not found"}, status=404)

        expense_data_serializers = ExpenseMasterSerializer(data=input_data)

        # handle incomplete and invalid inputs
        if not expense_data_serializers.is_valid():
            return Response({"error": expense_data_serializers.errors}, status=400)

        # update the expense
        expense_updated_data = ExpenseMasterSerializer(
            expense_obj, input_data, partial=True
        )

        if not expense_updated_data.is_valid():
            return Response({"error": expense_updated_data.errors}, status=400)

        expense_updated_data.save()
        return Response({"message": "expense updated"}, status=200)

    def delete(self, request, expense_id=None, *args, **kwargs):
        """method to delete specific expense"""

        if expense_id is None:
            return Response({"error": "Expense id is required"}, status=400)

        # get user id from jwt token
        user_id = request.user.id

        # check uuid
        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        student_obj = StudentMaster.objects.filter(id=validated_user_id).first()
        if student_obj is None:
            return Response({"error": "Student not found"}, status=400)

        # get specific expense
        expense_obj = ExpenseMaster.objects.filter(
            student=student_obj, id=expense_id
        ).first()
        if expense_obj is None:
            return Response({"error": "Expense not found"}, status=404)

        expense_obj.delete()
        return Response({"message": "expense deleted"}, status=200)


@api_view(["GET"])
# allowed permissions
@permission_classes([IsAuthenticated])
# @authentication_classes([decode_jwt_token])
# Swagger Schema for post api
@extend_schema(
    request=ExpenseMasterSerializer,
)
def get_total_expense(request, catogary=None, *args, **kwargs):
    user_id = request.user.id

    # check uuid
    user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
    if not user_id_serializer.is_valid():
        return Response({"error": user_id_serializer.errors}, status=400)

    validated_user_id = user_id_serializer.validated_data.get("id")
    student_obj = StudentMaster.objects.filter(id=validated_user_id).first()
    if student_obj is None:
        return Response({"error": "Student not found"}, status=400)

    if catogary is None:
        expense_obj = (
            ExpenseMaster.objects.filter(student=student_obj)
            .values("amount")
            .annotate(total_amount=Sum("amount"))
        )

        return Response(expense_obj, status=200)

    # get total expenses by catogary
    processed_catogary = catogary.lower().replace(" ", "_")
    expense_objs = (
        ExpenseMaster.objects.filter(
            student=student_obj, expense_catogary=processed_catogary
        )
        .values("amount")
        .annotate(total_amount=Sum("amount"))
    )

    return Response(expense_objs, status=200)
