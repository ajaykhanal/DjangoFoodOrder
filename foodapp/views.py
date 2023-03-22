from django.shortcuts import render,redirect
from .models import Food
from .models import Category
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import (
                                  authenticate,
                                  logout ,
                                  login
                              )
from .models import Cart,Order,OrderItem
from django.http import JsonResponse

# Create your views here.

def indexView(request):
    categories= Category.objects.all();
    categoryId= request.GET.get('category');
    if categoryId:
        foods= Food.objects.filter(category=categoryId)
    else:
        foods= Food.objects.all();
    
    return render(request,'index.html',{'foods':foods,'categories':categories})


def signupView(request):
    categories= Category.objects.all();
    categoryId= request.GET.get('category');
    if categoryId:
        foods= Food.objects.filter(category=categoryId)
    else:
        foods= Food.objects.all();

    form= CreateUserForm();
    if request.method == "POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            messages.success(request,"User Registration Successfully !!")
    return render(request,'signup.html',{'form':form,'foods':foods,'categories':categories})


def loginView(request):
    categories= Category.objects.all();
    categoryId= request.GET.get('category');
    if categoryId:
        foods= Food.objects.filter(category=categoryId)
    else:
        foods= Food.objects.all();


    if request.method == "POST":
        email= request.POST.get('email')
        password= request.POST.get('password')
        username = User.objects.get(email=email.lower()).username 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Loggedin Successfully !!")
            request.session['user_id']= user.id
            request.session['user_email']= user.email
            return redirect('/profile')
        else :
            messages.warning(request, "Invalid Credentials !!")
    return render(request,'login.html',{'foods':foods,'categories':categories})


def logoutView(request):
    logout(request)
    messages.success(request,"Logged out successfully !!")
    return redirect('/')


def profileView(request):
    categories= Category.objects.all();
    categoryId= request.GET.get('category');
    if categoryId:
        foods= Food.objects.filter(category=categoryId)
    else:
        foods= Food.objects.all();


    return render(request,'profile.html',{'foods':foods,'categories':categories})

def foodDetail(request,id):
    categories= Category.objects.all();
    categoryId= request.GET.get('category');
    if categoryId:
        foods= Food.objects.filter(category=categoryId)
    else:
        foods= Food.objects.all();


    food_detail= Food.objects.get(id=id);
    return render(request,'food_detail.html',{'food_detail':food_detail,'foods':foods,'categories':categories})


def addToCart(request):
    # print("Ok");
    if request.method == "POST":
        if request.user.is_authenticated:
            food_id= int(request.POST['food-id'])
            food_check= Food.objects.get(id=food_id)
            if(food_check):
                if(Cart.objects.filter(user=request.user.id, food=food_id)):
                    return JsonResponse({"status":"Food Already in Cart"});
                    
                else:
                    food_qty= int(request.POST['food-qty'])
                    Cart.objects.create(user=request.user, food_id=food_id, food_qty=food_qty)
                    return JsonResponse({"status":"Food Added in Cart"});
                    
        else:
            return JsonResponse({"status":"Login to Continue"}); 
    return redirect("/")


def cartView(request):
    cart= Cart.objects.filter(user=request.user)
    return render(request,'cart.html',{'cart':cart})


def updateCartView(request):
    if request.method=="POST":
        food_id= int(request.POST['food-id']);
        if(Cart.objects.filter(user=request.user, food_id=food_id)):
            food_qty= int(request.POST['food-qty']);
            cart= Cart.objects.get(user=request.user, food_id=food_id);
            cart.food_qty= food_qty;
            cart.save();
            return JsonResponse({"status":"Cart Updated"});
    return redirect("/");


def deleteCartView(request):
    if request.method=="POST":
        food_id= int(request.POST['food-id']);
        if(Cart.objects.filter(user=request.user, food_id=food_id)):
            cartitem= Cart.objects.get(user=request.user, food_id=food_id);
            cartitem.delete();
            return JsonResponse({"status":"Food Item Deletedd"});
    return redirect("/");


def checkoutView(request):
    cartItems= Cart.objects.filter(user=request.user);
    totalprice= 0;
    for item in cartItems:
        totalprice += item.food.price * item.food_qty;
    return render(request,"checkout.html",{'totalprice':totalprice,'cartItems':cartItems});


def placeanOrderView(request):
    if request.method=="POST":
        neworder= Order()
        neworder.user= request.user
        neworder.fname= request.POST.get('fname')
        neworder.lname= request.POST.get('lname')
        neworder.email= request.POST.get('email')
        neworder.phone= request.POST.get('phone')
        neworder.city= request.POST.get('city')
        neworder.address= request.POST.get('address')
        cart= Cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price= cart_total_price + item.food.price * item.food_qty 
        neworder.total_price= cart_total_price;
        neworder.save();
        neworderitems= Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order= neworder,
                food= item.food,
                price= item.food.price,
                quantity= item.food_qty,
            )
        Cart.objects.filter(user=request.user).delete();
        return redirect("/my-orders");
        messages.success(request,"Your Order has been placed successfully ! We Will Contact you as soon as possible !!");
    return redirect("/");


def myOrdersView(request):
    orderitems= Order.objects.filter(user=request.user);
    return render(request,"orders.html",{'orderitems':orderitems});

def viewOrderItems(request):
    order= Order.objects.filter(user= request.user).first();
    orderitems= OrderItem.objects.filter(order=order);
    return render(request,"viewordersitem.html",{'orderitems':orderitems,'order':order});
