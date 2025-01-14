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


    class EmployeeType(models.TextChoices):
        select_employee_type = 'Click to select', 'Click to select'
        dr = 'DR', 'DR'
        reception = 'RECEPTION', 'RECEPTION'


    class GenderClinicalEmployee(models.TextChoices):
        select_gender = 'Click to select', 'Click to select'
        male = 'Male', 'Male'
        female = 'Female', 'Female'



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

    employee_type = models.CharField(
        max_length=50,
        choices=EmployeeType.choices,
        default='Click to select'
    )

    gender_employee = models.CharField(
        max_length=50,
        choices=GenderClinicalEmployee.choices,
        default='Click to select'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.employee_type}"

class DRClinicalEmployee(AbstractClinicalEmployee):
    class Meta:
        verbose_name = "DR"
        verbose_name_plural = "DR's"

    class DrSpecialityType(models.TextChoices):
        select_speciality = 'Click to select', 'Click to select'
        s1 = 'SPECIALITY1', 'SPECIALITY1'
        s2 = 'SPECIALITY2', 'SPECIALITY2'
        s3 = 'SPECIALITY3', 'SPECIALITY3'
        s4 = 'SPECIALITY4', 'SPECIALITY4'
        s5 = 'SPECIALITY5', 'SPECIALITY5'
        s6 = 'SPECIALITY6', 'SPECIALITY6'


    medical_order_ID = models.CharField(
        _("Medical Order ID"),
        unique=True,
        null=False,
        help_text=_("A unique identifier for the medical order assigned to this user. This ID is used to track the user's medical orders.")
    )

    speciality_type = models.CharField(
        max_length=50,
        choices=DrSpecialityType.choices,
        default='Click to select'
    )

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name} {self.medical_order_ID}"


class ReceptionsClinicalEmployee(AbstractClinicalEmployee):
    class Meta:
        verbose_name = "Reception Assistant"
        verbose_name_plural = "Reception's Assistant"

    def __str__(self):
        return f"(Reception) {self.first_name} {self.last_name}"