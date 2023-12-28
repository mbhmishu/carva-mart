from django import forms
from PaymentApp.models import BillingAddress, OrderMsg



class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address', 'zipcode', 'city', 'country']


class OrderMsgForm(forms.ModelForm):
    class Meta:
        model = OrderMsg
        fields = ['driscribe_your_customize', 'Attach_image', 'provid_any_link',]