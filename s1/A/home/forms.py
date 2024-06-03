from django import forms
from .models import Tire

class Add_Porduct_Form(forms.Form):
    add_form_name = forms.CharField()
    add_form_description = forms.CharField()
    add_form_price = forms.IntegerField()

class Tire_Update_form(forms.ModelForm):
    class Meta:
        model = Tire
        fields = ('tire_name' , 'tire_description' , 'tire_price')    


class ContactUsForm(forms.Form):                            #could be initialliezed with Forms.ModelForm
    form_contact_name = forms.CharField(max_length=20)
    form_contact_phone = forms.CharField(max_length=15)
    form_contact_body = forms.CharField(max_length=500)
    form_contact_email = forms.EmailField()        