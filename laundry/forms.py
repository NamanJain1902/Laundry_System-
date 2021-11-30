from django import forms
from .models import BLaundry, GLaundry


class BOrderForm(forms.ModelForm):
    class Meta:
        model = BLaundry
        fields = '__all__'
        exclude = ['student']
    
    def clean(self):
        cleaned_data = super().clean()
        
        clothes_count = 0
        for field in self.fields:
            if (cleaned_data.get(field)) is not None:
                clothes_count += (int)(cleaned_data.get(field))
                
            if clothes_count > 10:
                raise forms.ValidationError('Invalid count', code='invalid')

class GOrderForm(forms.ModelForm):
    class Meta:
        model = GLaundry
        fields = '__all__'
        exclude = ['student']

    def clean(self):
        cleaned_data = super().clean()
        
        clothes_count = 0
        for field in self.fields:
            if (cleaned_data.get(field)) is not None:
                clothes_count += (int)(cleaned_data.get(field))
                
            if clothes_count > 10:
                raise forms.ValidationError('Invalid count', code='invalid')
