from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from decimal import Decimal

from groceryproducts.models import category
from groceryproducts.models import Product
from groceryproducts.models import Cart, CartItem

def SignUpPage(request):
    status=''
    status1=''
    if request.method == "POST":
        uname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')

        status1="Password doesn't match!!"


        if pass1!=pass2:
            return render(request,"signup.html",{'status1':status1})
        else:
            try:
                existing_user = User.objects.get(email=email)
                status="<p style='color:red';>User already exists!! Please Sign in</p>"
            except User.DoesNotExist:    
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                status="<p style='color:green';>Your Account has been created successfully! &#128512;</p>"
            
    return render(request,"signup.html",{'status':status})

def LoginPage(request):
    status2=''
    if request.method == "POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username, password=pass1)

        status2="Username or Password is incorrect"

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'status2':status2})
        
    return render(request,"login.html")


# //only authenticated user can access it
@login_required(login_url="/login/") 
def home(request):
    categories = category.objects.all()
    if request.user.is_superuser:
        message = "Welcome Admin!"
    else:
        message = "Welcome " + request.user.username + "!"
        
    context = {
        'categories': categories,
        'message': message
    }
    
    return render(request, "home.html", context)


def LogoutPage(request):
    logout(request)
    return redirect('login')

def Products(request, product_id=None):
    if product_id:
        product = Product.objects.get(id=product_id)
        print(product)  # add this line to check if the product object is being retrieved
        context = {'product': product}
    else:
        products = Product.objects.all()
        context = {'products': products}
    return render(request, 'product.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

from decimal import Decimal

def cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.product.product_price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)
def delete_item(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Perform deletion logic here
    product.delete()
    return redirect('cart')  

def payment(request):
    return render(request, 'payment.html')