from django.shortcuts import render , redirect
from .models import Tire , ContactForm
from .forms import Add_Porduct_Form , Tire_Update_form , ContactUsForm
from django.contrib import messages


def home(request):
    template_name = 'home_app/home.html'

    if request.method == 'GET' :
        products = Tire.objects.all()

    return render(request , template_name , context={'products': products})



def add_product(request):
    template_name = 'home_app/add_product.html'
    
    if request.method == 'POST':
        form = Add_Porduct_Form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Tire.objects.create(tire_name=cd['add_form_name'] , tire_description=cd['add_form_description'] , tire_price=cd['add_form_price'])
            messages.add_message(request , messages.SUCCESS , 'successfully created' , 'success')
            redirect("home:home")
        else :
            messages.add_message(request , messages.ERROR , 'invalid credentials sent' , 'danger')    
    else :        
        form = Add_Porduct_Form()
    return render(request , template_name , context={'form' : form} )


def product_detail(request , **kwargs):
    product_id = kwargs['product_id']
    template_name = 'home_app/detail.html'

    product = Tire.objects.get(pk=product_id)
    return render(request , template_name , context={'product' : product} )


def product_delete(request , product_id):
    try:
        Tire.objects.get(pk=product_id).delete()
        messages.add_message(request , messages.SUCCESS , 'success')
    except:
            messages.error(request , messages.ERROR , 'danger')
    return redirect('home:home')       


def product_update(request , product_id):
    product = Tire.objects.get(pk=product_id)
    template_name = 'home_app/update_product.html'

    if request.method == 'POST':
        form = Tire_Update_form (request.POST , instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , 'successfully updated' , 'success')
            return redirect('home:detail' , product_id) #product_id is the <int:product_id>
    else :
        form = Tire_Update_form(instance=product)   
    return render(request , template_name , context={"form" : form})   



def contact (request):
    template_name = 'home_app/contact_form.html'
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
                cd = form.cleaned_data
                ContactForm.objects.create(contact_name=cd['form_contact_name'] , contact_phone=cd['form_contact_phone'] , contact_body=cd['form_contact_body'] , contact_email=cd['form_contact_email'])
                messages.add_message(request , messages.SUCCESS , 'successfully submitted' , 'success')
                return redirect('home:home')
        else:
            messages.add_message(request , messages.ERROR , 'there was an error' , 'danger')
            return redirect('home:contact')
    else : 
        form = ContactUsForm()
        return render (request , template_name , context={'form':form})