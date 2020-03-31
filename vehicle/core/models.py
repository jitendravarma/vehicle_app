from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.

vehicle_type = (
    ('Two', 'Two'),
    ('Three', 'Three'),
    ('Four', 'Four'),
)

user_type = (
    ('user', 'user'),
    ('admin', 'admin'),
    ('super_user', 'super_user'),
)


class BaseUserProfile(AbstractUser):
    """
    BaseUserProfile inherited from abstract user, set user type and create
    respective profile
    """

    middle_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(choices=user_type, max_length=10, default='user')

    class Meta:
        verbose_name = "Base User Profile"
        verbose_name_plural = "Base User Profiles"

    @property
    def fullname(self):
        if self.last_name and self.first_name:
            return "%s %s" % (self.first_name, self.last_name)
        elif self.first_name:
            return "%s " % (self.first_name)
        else:
            return "%s " % (self.email)


class SuperAdminUser(models.Model):
    user = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Super Admin"
        verbose_name_plural = "Super Admins"

    def __str__(self):
        return f"{self.user.email}, {self.user.user_type}"


class AdminUser(models.Model):
    user = models.ForeignKey(BaseUserProfile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"

    def __str__(self):
        return f"{self.user.email}, {self.user.user_type}"


class Vehicle(models.Model):

    number = models.CharField(max_length=50, blank=True, null=True)
    unit_type = models.CharField(choices=vehicle_type,
                                 max_length=10, blank=True, null=True)
    model = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.number}, {self.unit_type}, {self.description}, {self.model}"

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
