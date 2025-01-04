import jwt
from datetime import datetime, timedelta
from pathlib import os
from django.conf import settings

JWT_SECRET = settings.JWT_SECRET


def generate_jwt_token(user_id, JWT_SECRET, expiration_minutes=60):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes=expiration_minutes),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token


def generate_refresh_token(user_id, JWT_SECRET, expiration_days=7):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(days=expiration_days),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token
