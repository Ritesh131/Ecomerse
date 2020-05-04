from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexhome'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('forgetpass', views.forgetpass, name='fogetpass'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='ContactUs'),
    path('tracker', views.tracker, name='TrackOrderStatus'),
    path('search', views.search, name='Search'),
    path('products/<int:myid>', views.productview, name='ProductView'),
    path('cart', views.cart, name='CartPage'),
    path('checkout', views.checkout, name='CheckoutPage'),
    # path('mail', views.sendmails, name='mail'),
    path('productapi', views.productapi, name='Productapi'),
    path('productpostapi', views.productpostapi, name='Productpostapi')
]
