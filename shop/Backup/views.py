from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login
from django.contrib.auth import logout as django_logout
from math import ceil

# Create your views here.
def index(request):
    produts = Product.objects.all()
    n = len(produts)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'produts': produts, 'no_slide':nslides, 'range': range(0,nslides)}
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