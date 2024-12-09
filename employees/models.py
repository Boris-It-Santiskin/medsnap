from dataclasses import field

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

    contact_number = models.CharField()

    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )


    #employee_type = models.CharField(choices=EmployeeType, default='DR')


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