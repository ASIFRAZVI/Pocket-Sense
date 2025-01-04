from django.db import models
from apps.base.models import BaseModel
from .student import StudentMaster


class OtpMaster(BaseModel):
    user = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    otp = models.IntegerField()
    is_used = models.BooleanField(default=False)

    class Meta:
        db_table = "otp_master"
