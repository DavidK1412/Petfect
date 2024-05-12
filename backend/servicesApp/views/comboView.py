from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authApp.security.token_validator import validate_admin


from servicesApp.models.combo import Combo
from servicesApp.serializers.comboSerializer import ComboSerializer


class ComboView(generics.GenericAPIView):
    serializer_class = ComboSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        combos = Combo.objects.all()
        serializer = ComboSerializer(combos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ComboSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
