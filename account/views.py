from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, OTPSerializer
from .utils import generate_otp
from django.utils import timezone
from datetime import timedelta
import jwt
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the My API😄😃😄😃")

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']).exists():
                return Response({"message": "Email already registered."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"message": "Registration successful. Please verify your email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestOtpView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "Email not registered."}, status=status.HTTP_400_BAD_REQUEST)
        
        otp = generate_otp()
        user.otp = otp
        user.otp_created_at = timezone.now()
        user.save()

        # Send OTP via email
        subject = 'Your OTP Code'
        message = f'Your OTP code is {otp}'
        from_email = settings.EMAIL_HOST_USER

        try:
            send_mail(subject, message, from_email, [email])
        except Exception as e:
            return Response({"message": "Failed to send OTP email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "OTP sent to your email."}, status=status.HTTP_200_OK)

class VerifyOtpView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"message": "Email not registered."}, status=status.HTTP_400_BAD_REQUEST)

            if user.otp != otp or (timezone.now() - user.otp_created_at) > timedelta(minutes=5):
                return Response({"message": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)
            
            user.is_verified = True
            user.save()

            token = jwt.encode({"email": email}, settings.SECRET_KEY, algorithm='HS256')

            return Response({"message": "Login successful.", "token": token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
