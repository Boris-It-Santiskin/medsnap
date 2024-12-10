# Generated by Django 5.1.3 on 2024-12-09 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('services', '0002_services_dr_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='customer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='customer.customers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('CANCELED', 'CANCELED'), ('CONFIRMED', 'CONFIRMED'), ('DONE', 'DONE')], default='PENDING'),
        ),
    ]