from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from authApp.serializers.loginSerializer import LoginSerializer


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if user is None:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.email_verified:
            return Response({'error': 'Email not verified'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        refresh['role'] = user.role.name
        refresh['id'] = str(user.id)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
