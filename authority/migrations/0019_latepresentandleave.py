# Generated by Django 4.1.5 on 2023-03-13 19:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0018_leavetype_salary_diduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatePresentAndLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed_time', models.DurationField()),
                ('allowed_late', models.PositiveIntegerField()),
                ('allowed_leave', models.PositiveIntegerField()),
                ('late_salary_cut', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('leave_salary_cut', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
