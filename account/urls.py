from django.urls import path
from .views import RegisterView, RequestOtpView, VerifyOtpView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('request-otp/', RequestOtpView.as_view(), name='request-otp'),
    path('verify-otp/', VerifyOtpView.as_view(), name='verify-otp'),
]
