from django import forms

class UserRegisterationForm(forms.Form):
    register_form_username = forms.CharField(max_length=20) 
    register_form_password = forms.PasswordInput()
    register_form_email = forms.EmailField()

class UserLoginForm(forms.Form):
    login_form_username = forms.CharField(max_length=20) 
    login_form_password = forms.PasswordInput()
    login_form_email = forms.EmailField()
