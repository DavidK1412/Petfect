from authApp.models.code import Code
from rest_framework import serializers

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer
from authApp.security.code_generator import generate_code
from emailApp import EmailService, Templates


class CodeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Code
        fields = ['user', 'code', 'created_at']

    def create(self, validated_data):
        user_id = validated_data.pop('request_user')
        user = User.objects.get(id=user_id)
        if not user:
            raise serializers.ValidationError('User not found')
        validated_data['code'] = generate_code()
        code = Code.objects.create(request_user=user, **validated_data)
        if not code:
            raise serializers.ValidationError('Code not created')
        email_data = {
            'to': user.email,
            'subject': 'Código de verificación',
            'text': 'Tú código para entrar en petfect!',
            'data': {
                'code': code.code,
                'user': user
            }
        }
        EmailService.send_email(Templates.AUTH_CODE, email_data)
        return code

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
