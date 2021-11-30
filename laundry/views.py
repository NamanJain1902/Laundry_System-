from django import forms
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import BLaundry, GLaundry
from .forms import BOrderForm, GOrderForm
from django.contrib import messages
import datetime
from django.db.models import Q
# Create your views here.

def indexView(request):

    return render(request, 'laundry/index.html')


def placeOrder(request):
    if request.user.groups.filter(name='Student').exists():
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
        user = request.user.studentprofile
        if request.method == 'POST':
            if str(user.gender) == 'Male':
                if BLaundry.objects.filter(student__icontains=user, date__range=(today_min, today_max)) is not None:
                    messages.success(request, "Your order has been placed already.")
                    return redirect('laundry-place-order')

                form = BOrderForm(request.POST, instance=BLaundry(student=user))

                if form.is_valid():
                    form.save()
                    messages.success(request, "Your order has been placed successfully.")
                    return redirect('laundry-order-history')
                else:
                    messages.error(request, "Max 10 clothes allowed!")
                    return redirect('laundry-place-order')
            elif str(user.gender) == 'Female':
                form = GOrderForm(request.POST, instance=GLaundry(student=user))
                if form.is_valid():
                    form.save()
                    messages.success(request, "Your order has been placed successfully.")
                    return redirect('laundry-order-history')
                else:
                    messages.error(request, "Max 10 clothes allowed!")
                    return redirect('laundry-place-order')
        else:  
            if str(user.gender) == "Male":  
                form = BOrderForm(instance=BLaundry(student=request.user.studentprofile))
            elif str(user.gender) == "Female":
                form = GOrderForm(instance=GLaundry(student=request.user.studentprofile))

        return render(request, 'laundry/place_order.html', {'form': form})
    return HttpResponseForbidden()


def orderHistory(request):

    if request.user.groups.filter(name='Student').exists():
        lset = BLaundry.objects.filter(student=request.user.studentprofile)

        context = {
            'lset' : lset,
        }
        
        return render(request, 'laundry/order_history.html', context)
    return HttpResponseForbidden()


def allOrders(request):
    
    user = request.user
    if user.groups.filter(name='Employee').exists():
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        
        if str(user.employeeprofile.gender) == "Male":
            lset = BLaundry.objects.filter(date__range=(today_min, today_max))        
        elif str(user.employeeprofile.gender) == "Female":
            lset = GLaundry.objects.filter(date__range=(today_min, today_max))

        if request.method == 'POST':    
            if request.POST.get('search_field', ''):
                search_field = request.POST.get('search_field', '')
                lset = lset.filter(Q(student__name__contains=search_field) | Q(student__college_id__contains=search_field))

        return render(request, 'laundry/orders_list.html', {'lset' : lset,})
    
    return HttpResponseForbidden()
