# Generated by Django 5.0.4 on 2024-05-12 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeesApp', '0001_initial'),
        ('servicesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='required_speciality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employeesApp.speciality'),
            preserve_default=False,
        ),
    ]
