# Generated by Django 4.2.5 on 2023-11-04 13:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_bookingofhotel_delete_testing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingofhotel',
            name='hotel_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookingofhotel',
            name='user',
            field=models.CharField(max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
    ]
