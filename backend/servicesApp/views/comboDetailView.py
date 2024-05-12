from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authApp.security.token_validator import validate_admin


from servicesApp.models.combo import Combo
from servicesApp.serializers.comboSerializer import ComboSerializer


class ComboDetailView(generics.GenericAPIView):
    serializer_class = ComboSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        try:
            combo = Combo.objects.get(pk=kwargs['pk'])
            if combo is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ComboSerializer(combo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Combo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            combo = Combo.objects.get(pk=kwargs['pk'])
            if combo is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            combo.delete()
            return Response(status=status.HTTP_200_OK)
        except Combo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        try:
            combo = Combo.objects.get(pk=kwargs['pk'])
            if combo is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ComboSerializer(combo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Combo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
