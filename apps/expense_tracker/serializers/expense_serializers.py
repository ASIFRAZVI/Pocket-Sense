from rest_framework import serializers

from apps.expense_tracker.models import ExpenseMaster

class ExpenseMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseMaster
        exclude = ['id', 'created']