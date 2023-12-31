# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hotel(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    ratings = models.FloatField(db_column='Ratings', blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    rating_description = models.TextField(db_column='Rating_Description', blank=True, null=True)  # Field name made lowercase.
    reviews = models.IntegerField(db_column='Reviews', blank=True, null=True)  # Field name made lowercase.
    star_rating = models.IntegerField(db_column='Star_Rating', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    nearest_landmark = models.TextField(db_column='Nearest_Landmark', blank=True, null=True)  # Field name made lowercase.
    distance_to_landmark = models.TextField(db_column='Distance_to_Landmark', blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    tax = models.IntegerField(db_column='Tax', blank=True, null=True)  # Field name made lowercase.
    total_amt = models.TextField(db_column='Total amt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotel'
