from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



class Application_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    email = models.CharField(unique=True, default="", max_length=200)
    password = models.CharField(max_length=50)
    phone_no = models.CharField(default="", max_length=50)
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=250, default="")
    otp = models.CharField(max_length=200, null=True)
    otp_gen_time = models.CharField(max_length=200, null=True)
    user_type = models.CharField(max_length=200, null=True)
    token = models.CharField(max_length=200, default="")



    def __str__(self):
        st = "%s - %s" % (self.user_id, self.first_name)
        return st
class Client(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
