from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    prod_id = models.AutoField
    product_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=60, default="")
    price = models.IntegerField(default=0)
    desc = RichTextField(max_length=500, default="")
    image = models.ImageField(upload_to="shop/images/productimages", default="")
    image1 = models.ImageField(upload_to="shop/images/productimages", default="")
    image2 = models.ImageField(upload_to="shop/images/productimages", default="")
    image3 = models.ImageField(upload_to="shop/images/productimages", default="")
    pub_date = models.DateField(default="")

    def __str__(self):
        return self.product_name

    def show_image(self):
        return format_html(f"<img src='/media/{self.image}' width='100px' height='100px' >")

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.IntegerField()
    query = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

    # Creating User Model
class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.username

    # Creating Order model
class Order(models.Model):
    user = models.CharField(max_length=100, default="")
    user_name = models.CharField(max_length=100, default="")
    user_email = models.EmailField()
    ship_address = models.CharField(max_length=200, default="")
    bill_address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=40, default="")
    zip_code = models.IntegerField()
    phone_number = models.IntegerField()

