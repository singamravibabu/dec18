# Generated by Django 5.1.4 on 2025-01-07 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_learning', '0006_employee_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='employee_learning.employee')),
                ('tel', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
