from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import (
    UserRegisterForm, 
    UserUpdateForm,
    ProfileUpdateForm, 
    EmployeeProfileUpdateForm
)
from django.contrib.auth.decorators import login_required
from .models import Hostel, StudentProfile, EmployeeProfile

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='Student')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request ,f"Account created for {username}! Login and complete your profile :)")
            return redirect('login')    
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {"form" : form,})



@login_required
def profile(request):
    if request.user.groups.filter(name='Student').exists():
        try:
            profile = request.user.studentprofile
        except StudentProfile.DoesNotExist:
            profile = StudentProfile(user=request.user)

        if request.method == 'POST':    
            u_form = UserUpdateForm(request.POST,instance=request.user)
            p_form = ProfileUpdateForm(request.POST, 
                                    instance=profile)

            if p_form.is_valid():
                p_form.save()
                messages.success(request, "Your information has been updated successfully.")
                return redirect('user-profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=profile)

    elif request.user.groups.filter(name='Employee').exists():
        try:
            profile = request.user.employeeprofile
        except EmployeeProfile.DoesNotExist:
            profile = EmployeeProfile(user=request.user)
            
        if request.method == 'POST':
            p_form = EmployeeProfileUpdateForm(request.POST, 
                                    instance=profile)
        
            if p_form.is_valid():
                p_form.save()

                messages.success(request, "Your information has been updated successfully.")
                return redirect('user-profile')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = EmployeeProfileUpdateForm(instance=profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, 'accounts/profile.html', context)


# AJAX
@login_required
def load_hostels(request):
    gender_id = request.GET.get('gender_id')
    hostels = Hostel.objects.filter(gender_id=gender_id).all()
    return render(request, 'accounts/hostel_dropdown_list_options.html', {'hostels': hostels})
