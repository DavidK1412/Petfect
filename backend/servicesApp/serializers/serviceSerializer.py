from rest_framework import serializers

from servicesApp.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at', 'required_speciality']

    def create(self, validated_data):
        return Service.objects.create(**validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['required_speciality'] = {
            'id': instance.required_speciality.id,
            'name': instance.required_speciality.name
        }

        return rep
