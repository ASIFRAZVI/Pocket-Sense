import random


def generate_random_otp(length):
    otp = random.choices("0123456789", k=length)
    final_otp = "".join(map(str, otp))
    return final_otp
