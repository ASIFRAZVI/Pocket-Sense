from django.db import models
from apps.base.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser
from pocket_sense import utils


class StudentMaster(AbstractBaseUser, BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField()
    phone_number = models.BigIntegerField()
    roll_number = models.CharField(max_length=200)
    semister = models.CharField(max_length=200)
    section = models.CharField(max_length=10)
    college = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    default_payment_method = models.CharField(choices=utils.PaymentChoices, null=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    class Meta:
        db_table = "student_master"
