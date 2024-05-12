from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authApp.security.token_validator import get_user_id, get_client_id


from clientsApp.models.pet import Pet
from clientsApp.serializers.petSerializer import PetSerializer


class PetView(generics.GenericAPIView):
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        client_id = get_client_id(get_user_id(request.META.get('HTTP_AUTHORIZATION')[7:]))
        if str(kwargs['pk']) != str(client_id):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            pets = Pet.objects.all().filter(client=client_id)
            serializer = PetSerializer(pets, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
