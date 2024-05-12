from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from servicesApp.models.service import Service
from servicesApp.serializers.serviceSerializer import ServiceSerializer
from authApp.security.token_validator import validate_admin


class ServiceDetailView(generics.GenericAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        service = Service.objects.get(pk=kwargs['pk'])
        if service is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            service = Service.objects.get(pk=kwargs['pk'])
            if service is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ServiceSerializer(service, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            service = Service.objects.get(pk=kwargs['pk'])
            if service is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            service.delete()
            return Response(status=status.HTTP_200_OK)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
