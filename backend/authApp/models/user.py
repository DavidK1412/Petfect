from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
import uuid

from .roles import Role


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email', max_length=255, unique=True)
    password = models.CharField('password', max_length=256)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)

    def save(self, **kwargs):
        some_salt = 'V2lzaCBvbiBhbiBFeWVsYXNo'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    def verify_email(self):
        self.email_verified = True
        super().save()

    objects = UserManager()
    USERNAME_FIELD = 'email'
