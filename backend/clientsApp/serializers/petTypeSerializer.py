from clientsApp.models.petType import PetType
from rest_framework import serializers


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = ['id', 'name', 'created_at']

    def create(self, validated_data):
        return PetType.objects.create(**validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
