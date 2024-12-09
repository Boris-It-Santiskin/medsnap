from email.policy import default
from random import choices
from snap.customer.models import Customers

from django.db import models

# Create your models here.
class Services(models.Model):

    class MedicalConsultations(models.TextChoices):
        micronutrientes = ['MICRONUTRIENTES', 'MICRONUTRIENTES', 30]
        general_medicine = ['GENERAL MEDICINE', 'GENERAL MEDICINE', 40]
        dermocosmetics = ['DERMOCOSMETICS', 'DERMOCOSMETICS', 45]
        estetics_and_cosmetics = ['ESTETICS AND COSMETICS', 'ESTETICS AND COSMETICS', 70]
        anti__aging_medical_consultation = ['ANTI-AGING MEDICAL CONSULTATION', 'ANTI-AGING MEDICAL CONSULTATION', 75]
        follow_up = ['FOLLOW-UP', 'FOLLOW-UP', 60]
        dermocosmetics_online = ['DERMOCOSMETICS ONLINE', 'DERMOCOSMETICS ONLINE', 60]
        estetics_and_cosmetics_online = ['ESTETICS AND COSMETICS ONLINE', 'ESTETICS AND COSMETICS ONLINE', 60]
        follow_up_anti_aging = ['FOLLOW-UP ANTI-AGING', 'FOLLOW-UP ANTI-AGING', 60]
        free_linical_assistance = ['FREE CLINICAL ASSISTANCE', 'FREE CLINICAL ASSISTANCE', 15]
        magress_online = ['MAGRESS_ONLINE', 'MAGRESS_ONLINE', 60]
        hair_medicine_and_trichology = ['HAIR MEDICINE AND TRICHOLOGY', 'HAIR MEDICINE AND TRICHOLOGY', 60]
        consultation_for_cosmetic_microsurgery = ['CONSULTATION FOR COSMETIC MICROSURGERY',
                                                  'CONSULTATION FOR COSMETIC MICROSURGERY', 60]

    scheduling_date = models.DateField()
    scheduling_time = models.TimeField()
    medication_consultation = models.CharField(choices=MedicalConsultations, default="Change a consultation")
    price = models.FloatField()


    scheduling_id = models.SlugField()
