from rest_framework import serializers
from clientsApp.models.pet import Pet
from clientsApp.models.petSize import PetSize
from clientsApp.models.petType import PetType
from clientsApp.models.client import Client
from clientsApp.serializers.clientSerializer import ClientSerializer
from clientsApp.serializers.petSizeSerializer import PetSizeSerializer
from clientsApp.serializers.petTypeSerializer import PetTypeSerializer


class PetSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    pet_size = PetSizeSerializer(read_only=True)
    pet_type = PetTypeSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = ['id', 'client', 'url_img', 'name', 'pet_size', 'pet_type', 'created_at', 'updated_at']

    def create(self, validated_data):
        client_id = self.initial_data.pop('client')
        pet_size_id = self.initial_data.pop('pet_size')
        pet_type_id = self.initial_data.pop('pet_type')
        client = Client.objects.get(user_id=client_id)
        pet_size = PetSize.objects.get(id=pet_size_id)
        pet_type = PetType.objects.get(id=pet_type_id)
        if not client:
            raise serializers.ValidationError('Client not found')
        if not pet_size:
            raise serializers.ValidationError('Pet size not found')
        if not pet_type:
            raise serializers.ValidationError('Pet type not found')
        pet = Pet.objects.create(client=client, size=pet_size, type=pet_type, **validated_data)
        if not pet:
            raise serializers.ValidationError('Pet not created')
        return pet

    def to_representation(self, instance):
        rep = {
            'id': instance.id,
            'client': ClientSerializer(instance.client).data['id'],
            'name': instance.name,
            'pet_size': PetSizeSerializer(instance.size).data['name'],
            'pet_type': PetTypeSerializer(instance.type).data['name'],
            'url_img': instance.url_img,
        }
        return rep

