from django.contrib import admin
from .models import Product
from .models import Contact
from .models import User

# New admin display feild for product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'pub_date', 'show_image']
    list_filter = ['pub_date', 'category', 'price',]
    search_fields = ['product_name', 'category', 'price', 'pub_date']
    list_per_page = 3


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(User)