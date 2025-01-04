from django.db.models.signals import post_save
from django.dispatch import Signal
from django.dispatch import receiver
from apps.authentication.models import StudentMaster
from apps.authentication.models.otp_master import OtpMaster
from apps.helpers.random_otp_generator import generate_random_otp
from django.core.mail import send_mail
from django.conf import settings


# create a profile after a student is created
@receiver(post_save, sender=StudentMaster)
def save_profile(sender, instance, created, **kwargs):
    if created:
        final_data = {"user": instance, "otp": generate_random_otp(length=6)}
        OtpMaster.objects.create(**final_data)


@receiver(post_save, sender=OtpMaster)
def save_profile(sender, instance, created, **kwargs):
    if created:
        subject = "OTP Verification Code"
        message = f"Hello {instance.user.name},\n\n welcome to POCKET SENSE\n\nYour OTP for verification is: {instance.otp}\n\nThank you!"
        recipient_list = [instance.user.email]

        # Send email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # from_email,
            recipient_list,
        )
