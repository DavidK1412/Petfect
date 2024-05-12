from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from clientsApp.models.client import Client
from authApp.models.user import User
from clientsApp.serializers.clientSerializer import ClientSerializer
from authApp.security.token_validator import validate_admin


class ClientDetailView(generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(pk=kwargs['pk'])
            if client is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClientSerializer(client)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            client = Client.objects.get(pk=kwargs['pk'])
            user = User.objects.get(pk=client.user.id)
            if client is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            client.delete()
            user.delete()
            return Response(status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(pk=kwargs['pk'])
            if client is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
