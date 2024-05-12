from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from employeesApp.models.speciality import Speciality
from employeesApp.serializers.specialitySerializer import SpecialitySerializer
from authApp.security.token_validator import validate_admin


class SpecialityDetailView(generics.GenericAPIView):
    serializer_class = SpecialitySerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        speciality = Speciality.objects.get(pk=kwargs['pk'])
        if speciality is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SpecialitySerializer(speciality)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            speciality = Speciality.objects.get(pk=kwargs['pk'])
            if speciality is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = SpecialitySerializer(speciality, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Speciality.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        if not validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            speciality = Speciality.objects.get(pk=kwargs['pk'])
            if speciality is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            speciality.delete()
            return Response(status=status.HTTP_200_OK)
        except Speciality.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
