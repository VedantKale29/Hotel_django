from django.contrib import admin
from .models import  Record,Hotel,Orders

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Record)
admin.site.register(Orders)