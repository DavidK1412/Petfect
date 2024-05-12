from rest_framework import generics, status
from rest_framework.response import Response

from authApp.models.roles import Role
from authApp.serializers.roleSerializer import RoleSerializer


class RoleDetailView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request, *args, **kwargs):
        try:
            role = Role.objects.get(pk=kwargs['pk'])
            if role is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = RoleSerializer(role)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
