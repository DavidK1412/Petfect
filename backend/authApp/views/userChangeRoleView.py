from rest_framework import status, generics
from rest_framework.response import Response

from authApp.serializers.userSerializer import UserSerializer
from authApp.security.token_validator import validate_admin
from authApp.models.user import User
from authApp.models.roles import Role


class UserChangeRoleView(generics.GenericAPIView):

    def patch(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        user_email = kwargs['email']
        user = User.objects.get(email=user_email)
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        role = Role.objects.get(id=request.data['role'])
        if not role:
            return Response({'error': 'Role not found'}, status=status.HTTP_404_NOT_FOUND)

        user.change_role(role)

        return Response({'Message:': 'Rol actualizado'}, status=status.HTTP_200_OK)
