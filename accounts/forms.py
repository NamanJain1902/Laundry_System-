from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Hostel, StudentProfile, Gender


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["thapar.edu"]
        if domain not in domain_list:
            raise forms.ValidationError("Please enter your TIET email address.")
        return data
    
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        exclude = ['user']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hostel'].queryset = Hostel.objects.none()

        if 'gender' in self.data:
            try:
                gender_id = int(self.data.get('gender'))
                self.fields['hostel'].queryset = Hostel.objects.filter(gender_id=gender_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Hostel queryset
        elif self.instance.pk:
            gender = self.instance.gender   
            self.fields['hostel'].queryset = gender.hostel_set.order_by('name')
