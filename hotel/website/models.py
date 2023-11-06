from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Hotel(models.Model):
    #id = models.IntegerField(blank=True, null=True)
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
    #image = models.ImageField(upload_to='', default="")

    class Meta:
        managed = False
        db_table = 'hotel'

    def __str__(self):
          return self.name

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
      
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")
    user = models.CharField(User,max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return(f"{self.name}")
    

class Payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    





