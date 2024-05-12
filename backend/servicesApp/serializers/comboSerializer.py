from rest_framework import serializers

from servicesApp.models.combo import Combo
from servicesApp.models.service import Service
from servicesApp.serializers.serviceSerializer import ServiceSerializer


class ComboSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Combo
        fields = ['id', 'name', 'description', 'price', 'created_at', 'updated_at', 'services']

    def create(self, validated_data):
        services = self.initial_data.pop('services')
        serviceInstances = []
        for service in services:
            service = Service.objects.get(id=service['id'])
            if not service:
                raise serializers.ValidationError('Service not found')
            serviceInstances.append(service)
        combo = Combo.objects.create(**validated_data)
        combo.services.set(serviceInstances)
        return combo

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        services = []
        for service in instance.services.all():
            services.append(ServiceSerializer(service).data)
        rep['services'] = services
        return rep
