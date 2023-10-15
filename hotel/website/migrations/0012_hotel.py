# Generated by Django 4.2.5 on 2023-10-11 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_delete_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('city', models.TextField(blank=True, db_column='City', null=True)),
                ('ratings', models.FloatField(blank=True, db_column='Ratings', null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('rating_description', models.TextField(blank=True, db_column='Rating_Description', null=True)),
                ('reviews', models.IntegerField(blank=True, db_column='Reviews', null=True)),
                ('star_rating', models.IntegerField(blank=True, db_column='Star_Rating', null=True)),
                ('location', models.TextField(blank=True, db_column='Location', null=True)),
                ('nearest_landmark', models.TextField(blank=True, db_column='Nearest_Landmark', null=True)),
                ('distance_to_landmark', models.TextField(blank=True, db_column='Distance_to_Landmark', null=True)),
                ('price', models.TextField(blank=True, db_column='Price', null=True)),
                ('tax', models.IntegerField(blank=True, db_column='Tax', null=True)),
                ('total_amt', models.TextField(blank=True, db_column='Total amt', null=True)),
                ('amount', models.IntegerField(blank=True, db_column='Amount', null=True)),
            ],
            options={
                'db_table': 'hotel',
                'managed': False,
            },
        ),
    ]
