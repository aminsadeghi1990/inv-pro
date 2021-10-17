from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json

class DateInput(forms.DateInput):
    input_type = 'date'

class UserLoginForm(forms.ModelForm):

    class Meta:
        model=User
        field=['username', 'password']


class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields = ['clientName', 'clientLogo', 'addressline1', 'province', 'postalCode', 'phoneNumber' ,'emailAddress', 'taxNumber']


 class ProductionForm(forms.ModelForm):
        model=Product
        fields=['title', 'description', 'quantity', 'price', 'currency'] 

class InvoiceForm(forms.ModelForm):
    dueDate = forms.DataField(
                        required = True,
                        label='Invoice Due'
                        widget=DataInput(attrs={'class': 'form-control'})

    class Meta:
        model=invoice
        field = ['title', 'number' , 'dueDate' , 'paymentTerms', 'status' , 'notes']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['clientName', 'clientLogo', 'addressline1', 'province', 'postalCode', 'phoneNumber' ,'emailAddress', 'taxNumber']


