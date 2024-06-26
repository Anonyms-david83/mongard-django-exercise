from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .forms import UserRegisterationForm , UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout


def user_register(request):
    template_name = 'account_app/register.html'

    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                User.objects.create_user(username=cd['register_form_username'] , password=cd['register_form_password'] , email=cd['register_form_email'])
                messages.add_message(request , messages.SUCCESS , 'registered succesfulyy' , 'success')
                return redirect('home:home')
            except:
                messages.add_message(request , messages.ERROR , 'there was a problem in registeration try again later' , 'danger')
    else :
        form = UserRegisterationForm()
        return render(request , template_name , context={'form':form} )
    
def user_login(request):
    template_name = 'account_app/login.html'
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['login_form_username'], password=cd['login_form_password'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS,'Logged in successfully' , 'success')
                return redirect('home:home')
            else:
                messages.add_message(request, messages.ERROR ,'Invalid credentials provided' , 'danger')
        else:
            messages.add_message(request, messages.ERROR ,'Form is not valid. Please check your input.' , 'danger')
    
    form = UserLoginForm()
    return render(request, template_name, context={"form": form})

def user_logout(request):
    try:
        logout(request)
        messages.add_message(request , messages.SUCCESS , 'logged out successfully' ,  'success')
    except:
        messages.add_message(request , messages.ERROR , 'there was a problem in your logging out ...' , 'danger')    
    return redirect('home:home')