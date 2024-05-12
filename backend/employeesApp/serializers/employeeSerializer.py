from rest_framework import serializers

from employeesApp.models.employee import Employee
from employeesApp.models.speciality import Speciality
from employeesApp.serializers.specialitySerializer import SpecialitySerializer


class EmployeeSerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone', 'image_url', 'created_at', 'updated_at', 'speciality']

    def create(self, validated_data):
        specialities = self.initial_data.pop('specialities')
        speciality_instances = []
        for speciality in specialities:
            speciality = Speciality.objects.get(id=speciality['id'])
            if not speciality:
                raise serializers.ValidationError('Speciality not found')
            speciality_instances.append(speciality)
        employee = Employee.objects.create(**validated_data)
        employee.specialities.set(speciality_instances)
        return employee

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        specialities = []
        for speciality in instance.specialities.all():
            specialities.append(SpecialitySerializer(speciality).data)
        rep['speciality'] = specialities
        return rep
