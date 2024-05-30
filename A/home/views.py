from django.shortcuts import render

def home(request):
    template_name = 'home_app/home.html'

    return render(request , template_name)