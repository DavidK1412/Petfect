from django.db import models
from .user import User


class Code(models.Model):
    request_user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
