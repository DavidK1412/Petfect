from django.db import models
from clientsApp.models import Client, Pet
from employeesApp.models import Employee
from servicesApp.models import Service, Combo
import uuid


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    taken = models.BooleanField(default=False)
    taken_by = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, related_name='appointments')
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
