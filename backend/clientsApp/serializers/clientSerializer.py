from rest_framework import serializers
from clientsApp.models.client import Client
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at', 'user']

    def create(self, validated_data):
        user_id = self.initial_data['user']
        user = User.objects.get(id=user_id)
        if not user:
            raise serializers.ValidationError('User not found')
        client = Client.objects.create(user=user, **validated_data)
        if not client:
            raise serializers.ValidationError('Client not created')
        return client

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        del rep['user']['password']
        return rep
