from dataclasses import field
from enum import UNIQUE

from django.db import models

# Create your models here.
class Customers(models.Model):

    full_name = models.CharField(
        max_length=256
    )

    email = models.EmailField(
        max_length=256,
        unique=True

    )

    tel = models.IntegerField(
        max_length = 14,
        unique=True

    )

    nif = models.IntegerField(
        max_length=9,
        unique=True
    )

    sns = models.IntegerField(
        max_length=9,
        unique = True
    )

    address = models.CharField(
        max_length=256
    )

    birthday = models.DateField()

    slug = models.SlugField(
        max_length=256,
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    created = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        # Generate the slug if it doesn't already exist
        if not self.slug:
            self.slug = self.create_slug()
        super().save(*args, **kwargs)

    def create_slug(self):
        return f"{self.tel}-{self.full_name}-{self.nif}"

    def  __str__(self):
        return f"{self.full_name} - {self.nif} - {self.slug}"


