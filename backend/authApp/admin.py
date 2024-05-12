from django.contrib import admin
from .models.user import User
from .models.roles import Role

# Register your models here.
admin.site.register(Role)
admin.site.register(User)
