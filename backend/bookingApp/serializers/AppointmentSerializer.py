from rest_framework import serializers

from bookingApp.models import Appointment
from clientsApp.models import Pet, Client
from employeesApp.models import Employee
from servicesApp.models import Service, Combo
from clientsApp.serializers import PetSerializer, ClientSerializer
from employeesApp.serializers import EmployeeSerializer
from servicesApp.serializers import ServiceSerializer, ComboSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Appointment
        fields = ['id', 'employee', 'taken', 'taken_by', 'pet', 'services', 'combo', 'price', 'date', 'time', 'created_at']

    def create(self, validated_data):
        services = self.initial_data.pop('services')
        serviceInstances = []
        for service in services:
            service = Service.objects.get(id=service['id'])
            if not service:
                raise serializers.ValidationError('Service not found')
            serviceInstances.append(service)
        appointment = Appointment.objects.create(**validated_data)
        appointment.services.set(serviceInstances)
        return appointment

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        services = []
        for service in instance.services.all():
            services.append(ServiceSerializer(service).data)
        rep['services'] = services
        return rep
