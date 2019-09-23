from django import forms
from django.contrib.auth.models import User
from testapp.models import cropdetail,irrigation,CropType
from django.core.exceptions import ValidationError
#crop add form
class SignUpForm(forms.ModelForm):
	class Meta:
		model=cropdetail
		fields=['name','cropname','cropquantity']
class Irrigation(forms.ModelForm):
	class Meta:
		model=irrigation
		fields=['CropStage']
class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
class CropType(forms.ModelForm):
	class Meta:
		model=CropType
		fields=['TypeOfCrop']
	
