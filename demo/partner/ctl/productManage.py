from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.http.response import HttpResponseRedirect
# from django.contrib import messages
from partner.forms import *
# from .models import Product
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home(request):
    return render(request,"partner/home.html")

# Sign-up view
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"account has been created successfully!!")
            return redirect("login")
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'partner/register.html', context)

@login_required
def display_product(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    return render(request,"partner/display.html", context)

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display")
    else:
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'partner/addProduct.html', context)

@login_required
def update(request,pk=None):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("display")
    context = {
        "form": form
    }
    
    return render(request, 'partner/addProduct.html', context)

@login_required
def delete(request,pk=None):
    product = Product.objects.filter(id=pk).delete()

    
    return redirect("display")

def profile(request,pk=None):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            #messages.success(request,f"account has been updated successfully!!")

            return redirect("display")
    
    context = {"form":form }
    return render(request,"partner/profile.html",context)
    