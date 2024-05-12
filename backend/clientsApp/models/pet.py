from django.db import models
from .client import Client
from .petSize import PetSize
from .petType import PetType

import uuid


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.ForeignKey(PetSize, on_delete=models.CASCADE)
    type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    url_img = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
