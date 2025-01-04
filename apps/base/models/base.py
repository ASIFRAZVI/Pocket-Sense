from django.db import models
import uuid


class BaseModel(models.Model):
    """
    Contains the last modified and the created fields, basically
    the base model for the entire app.
    """

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    # time tracking
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        abstract = True


