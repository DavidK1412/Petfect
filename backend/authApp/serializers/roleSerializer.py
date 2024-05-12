from authApp.models.roles import Role
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Role.objects.create(**validated_data)
