from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer
from clientsApp.models.client import Client
from clientsApp.serializers.clientSerializer import ClientSerializer


def get_token_data(token):
    token_backend = TokenBackend(algorithm= settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = token_backend.decode(token, verify=False)
    return valid_data


def validate_admin(token):
    valid_data = get_token_data(token)
    serializer = UserSerializer(User.objects.get(pk=valid_data['id']))
    if serializer.data['role']['id'] == 1:
        return True
    return False


def get_user_id(token):
    valid_data = get_token_data(token)
    return valid_data['id']


def get_client_id(user_id):
    client = Client.objects.get(user=user_id)
    return client.id
