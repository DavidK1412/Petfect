from rest_framework import status, generics
from rest_framework.response import Response

from authApp.models.code import Code
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class UserUpdateStateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, *args, **kwargs):
        user_email = kwargs['email']
        user = User.objects.get(email=user_email)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        code = Code.objects.get(code=request.data['code'])
        if not code:
            return Response({'error': 'Code not found'}, status=status.HTTP_404_NOT_FOUND)
        if user.id != code.request_user.id:
            return Response({'error': 'Code does not match with user'}, status=status.HTTP_400_BAD_REQUEST)
        user.verify_email()
        code.delete()
        return Response({'Message:': 'Usuario activado'}, status=status.HTTP_200_OK)
