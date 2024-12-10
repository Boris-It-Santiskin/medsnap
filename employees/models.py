from dataclasses import field

from autoslug.utils import slugify
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class AbstractClinicalEmployee(AbstractUser):

    class Meta:
        verbose_name = "Clinical Employee"
        verbose_name_plural = "Clinical Employees"

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='clinicalemployee_set',  # Custom related name
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='clinicalemployee_permissions_set',  # Custom related name
        blank=True
    )

    class EmployeeType(models.TextChoices):
        dr = 'DR', 'DR'
        reception = 'RECEPTION', 'RECEPTION'

    username = models.CharField(
        unique=False,
        blank=True,
        null=True
    )


    contact_number = models.CharField()

    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    employee_type = models.CharField(choices=EmployeeType, default='DR')




    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.employee_type}"

class DRClinicalEmployee(AbstractClinicalEmployee):
    class Meta:
        verbose_name = "DR"
        verbose_name_plural = "DR's"

    medical_order_ID = models.CharField(
        _("Medical Order ID"),
        unique=True,
        null=False,
        help_text=_("A unique identifier for the medical order assigned to this user. This ID is used to track the user's medical orders.")
    )


    def __str__(self):
        return f"Dr {self.first_name} {self.last_name} {self.medical_order_ID}"


class ReceptionsClinicalEmployee(AbstractClinicalEmployee):
    class Meta:
        verbose_name = "Reception Assistant"
        verbose_name_plural = "Reception's Assistant"

    def __str__(self):
        return f"(Reception) {self.first_name} {self.last_name}"