from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    context ={
        'products': Product.objects.all
    }

    return render(request,'items.html',context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []

    print(order)
    context ={
        'items': items,
        'order': order
    }
    return render(request,'cart.html',context)