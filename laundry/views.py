from django import forms
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import BLaundry, GLaundry
from .forms import BOrderForm, GOrderForm
from django.contrib import messages
import datetime
from django.db.models import Q
from accounts.models import Gender, Hostel, StudentProfile, EmployeeProfile
# Create your views here.



def indexView(request):

    return render(request, 'laundry/index.html')


def placeOrder(request):

    try:
        if request.user.groups.filter(name='Student').exists():
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
            
            user = request.user.studentprofile
            if request.method == 'POST':
                if str(user.gender) == 'Male':
                    # if BLaundry.objects.filter(student__icontains=user, date__range=(today_min, today_max)) is not None:
                    #     messages.success(request, "Your order has been placed already.")
                    #     return redirect('laundry-place-order')

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

    except StudentProfile.DoesNotExist:
        messages.info(request, 'Update Profile to proceed further')
        return redirect('user-profile')



def orderHistory(request):

    try:
        if request.user.groups.filter(name='Student').exists():

            if str(request.user.studentprofile.gender) == "Male":
                lset = BLaundry.objects.filter(student=request.user.studentprofile)
            else:
                lset = GLaundry.objects.filter(student=request.user.studentprofile)

            context = {
                'lset' : lset,
            }
            
            return render(request, 'laundry/order_history.html', context)
        return HttpResponseForbidden()
    
    except StudentProfile.DoesNotExist:
        messages.info(request, 'Update Profile to proceed further')
        return redirect('user-profile')


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

#display student details and last order of the student
def displayLastOrder(request):

    if request.user.groups.filter(name='Student').exists(): 
        try:
            profile = request.user.studentprofile

            if str(request.user.studentprofile.gender) == "Male":
                lset = BLaundry.objects.filter(student=request.user.studentprofile)
            else:
                lset = GLaundry.objects.filter(student=request.user.studentprofile)

            if lset:
                lastOrder = [lset[len(lset)-1]]
            else:
                lastOrder = []

            context1={
                "type":"Student",
                "user":request.user,
                "name":profile.name,
                "college_id": profile.college_id,
                "mobile_num":profile.mobile_num,
                "room_num":profile.room_num,
                "gender":profile.gender,
                "hostel":profile.hostel,
                "list":lastOrder
            }

            return render(request, 'laundry/lastOrder.html',context1)

        except StudentProfile.DoesNotExist:
            messages.info(request, 'Update Profile to proceed further')
            return redirect('user-profile')

    elif request.user.groups.filter(name='Employee').exists():
        try:
            profile = request.user.employeeprofile

            context1={
                "type":"Employee",
                "user":request.user,
                "name":profile.name,
                "employee_id": profile.employee_id,
                "mobile_num":profile.mobile_num,
                "gender":profile.gender,
                "hostel":profile.hostel,
                "list":None
            }

            return render(request, 'laundry/lastOrder.html',context1)

        except EmployeeProfile.DoesNotExist:
            messages.info(request, 'Update Profile to proceed further')
            return redirect('user-profile')
    else:
        return redirect('user-profile')
