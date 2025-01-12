from rest_framework.urls import path
from .views import StudentRegisteration, StudentLoginView,StudentLogoutView,VerifyStudent, resend_otp
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # register user
    path("signup/", StudentRegisteration.as_view(), name="register_student"),
    # login user
    path("signin/", StudentLoginView.as_view(), name="login_student"),
    # logout user
    path("signout/", StudentLogoutView.as_view(), name="logout_student"),
    # verify user
    path("verify/", VerifyStudent.as_view(), name="ativate_account"),
    # resend otp
    path("resend-otp/", resend_otp, name="resend_otp"),
    # simple jwt urls
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
