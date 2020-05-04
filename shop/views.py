from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login
from django.contrib.auth import logout as django_logout
from math import ceil
from django.views.generic.edit import FormView
from django.core.mail import send_mail, send_mass_mail, mail_admins, mail_managers
from django.core.serializers import serialize
import json

# Create your views here.
def index(request):
    slide1 = []
    produts = []
    bookcat = Product.objects.values('category')
    cats = {item['category'] for item in bookcat}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        slide1.append(prod[0:4])
        produts.append(prod[4:8])
    # produts = Product.objects.all()
    print(produts)
    params = {'produts': produts[0], 'slide1': slide1[0]}
    return render(request, 'shop/index.html', params)

        # Login page template
def login(request):
    if request.method == 'POST':
        # Get the post parameter
        username = request.POST['loginusername']
        password = request.POST['loginpass']

        user = authenticate(request ,username = username, password = password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Login")
            return redirect('indexhome')
        else:
            messages.error(request, "Invalid Credantial Provided")
            return redirect('indexhome')

            # Logout Function
def logout(request):
    django_logout(request)
    messages.success(request, "Successfully LogOut")
    return redirect('indexhome')

                # Register page template
def register(request):
    # userdata = User.objects.all()
    # useremail = []
    # for i in userdata:
    #    useremail.append(i.email)
    if request.method == 'POST':
        # Get the post parameter
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        confpassword = request.POST['pass2']

        # check email is exit or not
        if password != confpassword:
            messages.error(request, "Password is not match to confirm password")
            return redirect('indexhome')

        if len(password) <= 5 :
            messages.error(request, "Password is too short.")
            return redirect('indexhome')

        if len(username) <= 10 :
            messages.error(request, "UserName must contain character.")
            return redirect('indexhome')

        # create user
        user = User.objects.create_user(username, email, password)
        # Update fields and then save again
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, f"Hii {firstname + lastname} you are succesfully register with example.com")
        return redirect('indexhome')
    else:
        return HttpResponse('Sorry we found some error to register your account.Please try again')
    return render(request, 'shop/auth.html')

    # Forget Password Template

def forgetpass(request):
    # return HttpResponse('This is forgetpass')
    return render(request, 'shop/auth.html')

                      # About US page template
def about(request):
    # return HttpResponse('This is Aboutpages')
    return render(request, 'shop/about.html')


                     # Contact US page template
def contact(request):
    # return HttpResponse('This is Contact')
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
    return render(request, 'shop/contact.html')

                    # Contact US page emplate
def tracker(request):
    return render(request, 'shop/tracker.html')

                    # Search page emplate
def search(request):
    # return HttpResponse('This is Search')
    return render(request, 'shop/search.html')

                    # Productview page emplate
def productview(request, myid):
    #Fetching the Product Using Id
    product = Product.objects.filter(id=myid)
    param1 = {'product':product[0]}
    return render(request, 'shop/productview.html', param1)

                    # Cart page emplate
def cart(request):
    return HttpResponse('This is Cart')
    # return render(request, 'shop/cart.html')

                    # Checkout page emplate
def checkout(request):
    # return HttpResponse('This is Checkout')
    return render(request, 'shop/checkout.html')


# def sendmails(request):
    mail = send_mail('Test Subject', 'Hello! Hii', 'bajpairitesh878@gmail.com', ['bajpairitesh878@gmail.com'], fail_silently=False, html_message='How are you')
                
    if mail:
        return HttpResponse('mail')
    else:
        return Exception('Error')

def productapi(request):
    productdata = Product.objects.all()
    api = serialize('xml', productdata)

    return HttpResponse(api, content_type='text/xml')

def productpostapi(request, pk=None):
    if request.method == 'POST':
        productdata = Product(request.POST, request.FILES)
        if productdata.is_valid():
            productdata.save()
            productdata = {
                'success' : 'Form Submited Successfully',
                'productdata' : productdata
            }
        productdata = json.dump(productdata)
    else:
        if pk is None:
            productdata = Product.objects.all()
        else:
            productdata = Product.objects.filter(pk=pk)
        
    productdata = serialize('xml', productdata, use_natural_foreign_keys=True)

    # productdata = serialize('json', productdata)

    return HttpResponse(productdata, content_type='application/xml')