from django.db import models

# importing the necessary models from the respective apps
from apps.authentication.models import StudentMaster
from apps.base.models import BaseModel

# utils
from pocket_sense import utils


class ExpenseMaster(BaseModel):
    student = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    expense_catogary = models.CharField(choices=utils.CatogaryChoices)
    amount = models.FloatField()
    description = models.TextField()
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(choices=utils.PaymentChoices, null=True)

    class Meta:
        db_table = "expense_master"
