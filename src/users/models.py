from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)  # inheriting from django User

# creating userModel
# add required field only here
# first_name=None not required
from django.utils.datetime_safe import datetime


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name=None, password=None, is_active=True, is_admin=False,
                    is_staff=False):
        if not email:
            raise ValueError("User must have an email address")
        if not first_name:
            raise ValueError("User must have an first name")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        # built in method for built in User model
        user_obj.set_password(password)  # change your password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, first_name, last_name=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, first_name, last_name=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True
        )
        return user

    # keep this clean until it's not necessary


class User(
    AbstractBaseUser):  # can chage to anything it's our django class if you want you can change this whatever you wnat
    # username = models.CharField()#if we want we can still use this field
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)  # can log in
    staff = models.BooleanField(default=False)  # staff user not super user
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # now this is my usernamefield now  not no more userneme

    REQUIRED_FIELDS = ['first_name', 'last_name']  # required filelds with

    objects = UserManager()

    # those fields come during python manage.py createsuperuser

    def __str__(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        if self.last_name:
            return self.last_name  # if last_name is not necessary field
        return self.email

    def has_perm(self, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
