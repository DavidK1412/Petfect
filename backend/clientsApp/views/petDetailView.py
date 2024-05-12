from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authApp.security.token_validator import get_user_id, validate_admin, get_client_id


from clientsApp.models.pet import Pet
from clientsApp.serializers.petSerializer import PetSerializer
from clientsApp.models.petType import PetType
from clientsApp.models.petSize import PetSize


class PetDetailView(generics.GenericAPIView):
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        try:
            pet = Pet.objects.get(pk=kwargs['pk'])
            if pet is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            client_id = get_client_id(get_user_id(request.META.get('HTTP_AUTHORIZATION')[7:]))
            if pet.client.id != client_id or validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]) is False:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer = PetSerializer(pet)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            pet = Pet.objects.get(pk=kwargs['pk'])
            if pet is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if pet.client.id != get_user_id(request.META.get('HTTP_AUTHORIZATION')[7:]) or validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]) is False:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            pet.delete()
            return Response(status=status.HTTP_200_OK)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        try:
            pet = Pet.objects.get(pk=kwargs['pk'])
            if pet is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if pet.client.id != get_user_id(request.META.get('HTTP_AUTHORIZATION')[7:]) or validate_admin(request.META.get('HTTP_AUTHORIZATION')[7:]) is False:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer = PetSerializer(pet, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        pet_type = PetType.objects.get(pk=request.data['type'])
        if pet_type is None:
            return Response({'error': 'PetType not found'}, status=status.HTTP_404_NOT_FOUND)
        pet_size = PetSize.objects.get(pk=request.data['size'])
        if pet_size is None:
            return Response({'error': 'PetSize not found'}, status=status.HTTP_404_NOT_FOUND)
        request.data['client'] = get_user_id(request.META.get('HTTP_AUTHORIZATION')[7:])
        request.data['pet_type'] = pet_type.id
        request.data['pet_size'] = pet_size.id
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
