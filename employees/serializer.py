from rest_framework import serializers

from .employees.models import AbstractClinicalEmployee


class AbstractClinicalEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractClinicalEmployee