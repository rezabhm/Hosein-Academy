from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ...models import OtpCode, StudentInformation
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import random
import string
from django.utils import timezone
import requests  # Placeholder for SMS service


class SendOtpView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user exists or create new
        try:
            user = User.objects.get(username=phone_number)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=phone_number,
                password=''.join(random.choices(string.ascii_letters + string.digits, k=12))
            )

        # Generate 6-digit OTP
        otp_code = ''.join(random.choices(string.digits, k=6))

        # Save or update OTP
        OtpCode.objects.update_or_create(
            user=user,
            defaults={'code': otp_code, 'create_at': timezone.now()}
        )

        # Placeholder for SMS sending
        try:
            # Replace with your SMS service provider API
            sms_response = requests.post(
                'YOUR_SMS_PROVIDER_API',
                data={'phone': phone_number, 'message': f'Your OTP code is: {otp_code}'}
            )
            if sms_response.status_code != 200:
                return Response({'error': 'Failed to send OTP'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': f'SMS sending failed: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)


class VerifyOtpView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        if not phone_number or not code:
            return Response({'error': 'Phone number and code are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=phone_number)
            otp = OtpCode.objects.get(user=user)

            if not otp.is_valid():
                return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)

            if otp.code != code:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

            # Generate tokens
            refresh = RefreshToken.for_user(user)

            # Check if user is admin
            is_admin = user.is_staff or user.is_superuser

            # Check if student information exists
            has_student_info = StudentInformation.objects.filter(user=user).exists()

            # Delete OTP after successful verification
            otp.delete()

            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'is_admin': is_admin,
                    'has_student_info': has_student_info
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except OtpCode.DoesNotExist:
            return Response({'error': 'No OTP found'}, status=status.HTTP_404_NOT_FOUND)


class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            return Response({'access': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # Invalidate refresh token

            return Response({'message': 'Successfully logged out'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)