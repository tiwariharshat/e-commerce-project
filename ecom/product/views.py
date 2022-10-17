

from django.shortcuts import HttpResponseRedirect, redirect, render
from product.models import Product, SizeVariant
from account.models import Cart , CartItem
from django.http import HttpResponseRedirect



def get_products(request , slug):
    try:
        product = Product.objects.get(slug =slug)

        


        return render(request  , 'product/product.html' , context = {'product' : product})

    except Exception as e:
        print(e)


def add_to_cart(request , uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid = uid)
    user = request.user
    cart , _ =Cart.objects.get_or_create(user = user , is_paid =False)

    cart_item=CartItem.objects.create(cart =cart , product = product)

    if variant:
        variant =request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
        cart_item.size_variant = size_variant
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))