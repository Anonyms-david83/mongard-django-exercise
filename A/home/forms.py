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