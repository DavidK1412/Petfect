from django.db import models
import uuid

from employeesApp.models.speciality import Speciality


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    required_speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
