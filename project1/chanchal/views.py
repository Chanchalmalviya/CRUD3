from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from django.contrib import messages
from chanchal.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def regi_views(request):
    return render(request,'registration.html')

def product(request):
    p_data =Product.objects.all()
    return render(request,'product.html',{'p_data':p_data})

def view_add_product(request):
    return render(request,'add_product.html')

def ragistration(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already Exist")
        else:
            User.objects.create(name=name,email=email,password=password)
            return redirect("/")
        


def login(request):
    if request.method =='POST':
        email =request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj =User.objects.get(email=email)
            password = obj.password
            if check_password(user_password,password):
                 return redirect("/product/")
            else:
                messages.error(request,"Password incorrect")
                return redirect("/")
        else:
            messages.error(request,"Email is not registerd")
            return redirect("/")
    else:
        messages.error(request,"Please fill mail id and passworsd")
        return redirect("/") 


def add_product(request):
    if request.method =="POST":
        title = request.POST["title"]
        description = request.POST["description"]
        product_image = request.FILES.get("product_image") 
        Product.objects.create( title=title,description=description,product_image=product_image)
        messages.success(request,"Product added Successfully")
        return redirect("/product/")

def delete_product(request,pk):
    Product.objects.get(id=pk).delete()
    return redirect("/product/")

def productupdate(request,uid):
     user_obj = Product.objects.get(id=uid)
     return render(request,"update_product.html",{"user_obj":user_obj})

def Product_update(request):
    if request.method =="POST":
        uid = request.POST['uid']
        title =request.POST['title']
        description = request.POST['description']
        product_image = request.FILES.get("product_image") 
        product_obj = Product.objects.get(id=uid)
        product_obj.title=title
        product_obj.description=description
        if product_image:
            product_obj.product_image=product_image
        product_obj.save()
        return redirect("/product/")  



    
   
    

