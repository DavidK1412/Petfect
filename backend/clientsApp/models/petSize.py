from django.db import models


class PetSize(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
