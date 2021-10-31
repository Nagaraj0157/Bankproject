from django import forms
from .models import *
class registerform(forms.Form):
    name=forms.CharField()
    account_num=forms.CharField()
    ifsc=forms.CharField()
    mob_no=forms.IntegerField()
    location=forms.CharField()
    amount=forms.FloatField()
class loginform(forms.Form):
    account_num=forms.CharField()
    mob_no=forms.IntegerField()
class transactionform(forms.Form):
    your_acc_no=forms.CharField()
    acc_no=forms.CharField()
    amount=forms.FloatField()
class updateform(forms.ModelForm):
    class Meta:
        model=acc_details
        fields='__all__'
