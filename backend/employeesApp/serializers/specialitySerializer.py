from rest_framework import serializers

from employeesApp.models.speciality import Speciality


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Speciality.objects.create(**validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
