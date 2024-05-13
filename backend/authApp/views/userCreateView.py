from rest_framework import status, views
from rest_framework.response import Response

from authApp.serializers.roleSerializer import RoleSerializer
from authApp.serializers.userSerializer import UserSerializer
from authApp.serializers.codeSerializer import CodeSerializer
from authApp.security.token_validator import validate_admin
from authApp.models.user import User


class UserCreateView(views.APIView):
    code_serializer = CodeSerializer()
    role_serializer = RoleSerializer()

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            code_serializer = self.code_serializer.create({'request_user': user.id})
            if not code_serializer:
                return Response({'error': 'Code not created'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'Message:': 'Por favor, verifica tu e-mail'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
