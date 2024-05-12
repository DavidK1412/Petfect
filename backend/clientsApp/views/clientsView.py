from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from authApp.security.token_validator import validate_admin

from clientsApp.models.client import Client
from clientsApp.serializers.clientSerializer import ClientSerializer
from authApp.serializers.userSerializer import UserSerializer
from authApp.serializers.codeSerializer import CodeSerializer


class ClientCreateView(generics.ListCreateAPIView):
    code_serializer = CodeSerializer()

    def post(self, request, *args, **kwargs):
        request.data['role'] = 2
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            request.data['user'] = str(user.id)
            client_serializer = ClientSerializer(data=request.data)
            if client_serializer.is_valid():
                client_serializer.save()
                code_serializer = self.code_serializer.create({'request_user': user.id})
                if not code_serializer:
                    return Response({'error': 'Code not created'}, status=status.HTTP_400_BAD_REQUEST)
                return Response({'Message:': 'Por favor, verifica tu e-mail'}, status=status.HTTP_201_CREATED)
            return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        clients = Client.objects.all()
        clients = ClientSerializer(clients, many=True)
        return Response(clients.data, status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
