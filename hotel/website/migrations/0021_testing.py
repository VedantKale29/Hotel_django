# Generated by Django 4.2.5 on 2023-11-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.BooleanField(default=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]