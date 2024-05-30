from django.shortcuts import render
from .models import Tire


def home(request):

    if request.method == 'GET' :
        template_name = 'home_app/home.html'
        products = Tire.objects.all()

    return render(request , template_name , context={'products': products})