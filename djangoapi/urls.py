from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/request-otp/', views.RequestOtpView.as_view(), name='request-otp'),
    path('api/verify-otp/', views.VerifyOtpView.as_view(), name='verify-otp'),
]
