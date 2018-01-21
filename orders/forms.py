from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email','address','postal_code','city']

# class OrderCreateForm(forms.Form):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.IntegerField(required=True)
#     address = forms.CharField(required=True)
#     postal_code = forms.IntegerField(required=True)
#     city = forms.CharField(required=True)
#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].label = "Your First name:"
#         self.fields['last_name'].label = "Your Last name:"
#         self.fields['email'].label = "Your Email:"
#         self.fields['phone'].label = "Your Phone Number:"
#         self.fields['adress'].label ="Your Adress:"
#         self.fields['postal_code'].label ="Your Postal Code:"
#         self.fields['city'].label ="Your city:"