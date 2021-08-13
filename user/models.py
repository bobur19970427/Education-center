import os
from uuid import uuid4
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Create your models here.



def get_profile_photo_path(instance, filename):
    ext = str(filename).split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('profile_picture/', filename)


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Users must have a phone number!")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class Region(models.Model):
    name = models.CharField(_('Nomi'), max_length=255)

    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birth_date = models.DateTimeField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to=get_profile_photo_path,
                                      blank=True, null=True)
    region = models.ForeignKey(Region, verbose_name=_('Viloyati'),
                               on_delete=models.SET_NULL, blank=True, null=True)
    paid_till = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id', )

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'


    def __str__(self):
        return self.phone_number