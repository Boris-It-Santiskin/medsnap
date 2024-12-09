from email.policy import default
from random import choices


from django.db import models

# Create your models here.
class Services(models.Model):
    CONSULTATION_SPANDING_TIME = {
        'MICRONUTRIENTS': 30,
        'GENERAL_MEDICINE': 40,
        'DERMOCOSMETICS': 45,
        'ESTETICS_AND_COSMETICS': 70,
        'ANTI_AGING_CONSULTATION': 75,
        'FOLLOW_UP': 60,
        'DERMOCOSMETICS_ONLINE': 60,
        'ESTETICS_AND_COSMETICS_ONLINE': 60,
        'FOLLOW_UP_ANTI_AGING': 60,
        'FREE_CLINICAL_ASSISTANCE': 15,
        'MAGRESS_ONLINE': 60,
        'HAIR_MEDICINE_AND_TRICHOLOGY': 60,
        'COSMETIC_MICROSURGERY': 60,
    }

    class MedicalConsultations(models.TextChoices):
        MICRONUTRIENTS = 'MICRONUTRIENTS', 'Micronutrients'
        GENERAL_MEDICINE = 'GENERAL_MEDICINE', 'General Medicine'
        DERMOCOSMETICS = 'DERMOCOSMETICS', 'Dermocosmetics'
        ESTETICS_AND_COSMETICS = 'ESTETICS_AND_COSMETICS', 'Estetics and Cosmetics'
        ANTI_AGING_CONSULTATION = 'ANTI_AGING_CONSULTATION', 'Anti-aging Medical Consultation'
        FOLLOW_UP = 'FOLLOW_UP', 'Follow-up'
        DERMOCOSMETICS_ONLINE = 'DERMOCOSMETICS_ONLINE', 'Dermocosmetics Online'
        ESTETICS_AND_COSMETICS_ONLINE = 'ESTETICS_AND_COSMETICS_ONLINE', 'Estetics and Cosmetics Online'
        FOLLOW_UP_ANTI_AGING = 'FOLLOW_UP_ANTI_AGING', 'Follow-up Anti-aging'
        FREE_CLINICAL_ASSISTANCE = 'FREE_CLINICAL_ASSISTANCE', 'Free Clinical Assistance'
        MAGRESS_ONLINE = 'MAGRESS_ONLINE', 'Magress Online'
        HAIR_MEDICINE_AND_TRICHOLOGY = 'HAIR_MEDICINE_AND_TRICHOLOGY', 'Hair Medicine and Trichology'
        COSMETIC_MICROSURGERY = 'COSMETIC_MICROSURGERY', 'Consultation for Cosmetic Microsurgery'


    scheduling_date = models.DateField()
    scheduling_time = models.TimeField()
    medication_consultation = models.CharField(choices=MedicalConsultations, default="Change a consultation")
    price = models.FloatField()


    scheduling_id = models.SlugField()
