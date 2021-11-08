from django.shortcuts import render, redirect
from .models import BLaundry, GLaundry
from .forms import BOrderForm, GOrderForm
from django.contrib import messages
# Create your views here.

def indexView(request):

    return render(request, 'laundry/index.html')


def placeOrder(request):
    
    if request.method == 'POST':
        bo_form = BOrderForm(request.POST, instance=BLaundry(student=request.user))
        go_form = GOrderForm(request.POST, instance=GLaundry(student=request.user))

        if bo_form.is_valid():
            bo_form.save()
            messages.success(request, "Your order has been placed successfully.")
            return redirect('laundry-order-history')

        elif go_form.is_valid():
            go_form.save()
            messages.success(request, "Your order has been placed successfully.")
            return redirect('laundry-order-history')
    else:    
        bo_form = BOrderForm(instance=BLaundry(student=request.user))
        go_form = GOrderForm(instance=GLaundry(student=request.user))

    context ={
        'bo_form': bo_form,
        'go_form': go_form,
    }
    return render(request, 'laundry/place_order.html', context)


def orderHistory(request):
    
    lset = BLaundry.objects.filter(student=request.user)

    context = {
        'lset' : lset,
    }

    return render(request, 'laundry/order_history.html', context)


def allOrders(request):
    pass
