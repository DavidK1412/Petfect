from clientsApp.models.petSize import PetSize
from rest_framework import serializers


class PetSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSize
        fields = ['id', 'name', 'created_at', 'updated_at']

    def create(self, validated_data):
        return PetSize.objects.create(**validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
