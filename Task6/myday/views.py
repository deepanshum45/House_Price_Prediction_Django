from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myday.models import Product
from django.urls import reverse


# Create all products with one click
def newproduct(request):
    res=render(request,'newproduct.html')
    return res

def saveorder(request):
    pname=request.POST['pname']
    pprice=request.POST['pprice']
    poffer=request.POST['poffer']
    emp=Product(pname=pname,pprice=pprice,poffer=poffer)
    emp.save()
    url=reverse('productlist')
    return HttpResponseRedirect(url)


# Read all products
def productlist(request):
    product= Product.objects.all()
    res=render(request, 'product.html',{'product': product})
    return res

def updateproductform(request):
    id=request.GET['id']
    products=Product.objects.filter(id=id).values()
    res=render(request,'updateproductform.html',{'products':products[0]})
    return res


# Update product
def updateProduct(request):
    id =request.POST['id']
    pname =request.POST['pname']
    pprice =request.POST['pprice']
    poffer =request.POST['poffer']
    Product(id=id, pname=pname,pprice=pprice,poffer=poffer).save()
    url=reverse('productlist')
    return HttpResponseRedirect(url)

# Delete product
def deleteProduct(request):
    id=request.GET['id']
    pmp=Product.objects.filter(id=id)
    pmp.delete()
    url=reverse('productlist')
    return HttpResponseRedirect(url)