from rest_framework import serializers
from authApp.models.roles import Role
from authApp.models.user import User
from authApp.serializers.roleSerializer import RoleSerializer


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'role', 'email_verified']

    def create(self, validated_data):
        role = Role.objects.get(id=self.initial_data['role'])
        if not role:
            raise serializers.ValidationError('Role not found')
        user = User.objects.create(role=role, **validated_data)
        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['role'] = RoleSerializer(instance.role).data
        return rep
