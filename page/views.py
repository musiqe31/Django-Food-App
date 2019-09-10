from django.shortcuts import render
from .models import FoodPage
from django.core.mail import send_mail
# Create your views here.

def index(request):
    foods = FoodPage.objects.order_by('infoname')
    context = {
        'foodoftheday': foods
    }
    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def results(request):
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]

    send_mail(
        subject,
        "Inquiry:\n"+message,
        email,
        ["test"],
        fail_silently=False,
    )

    context = {
        "name": name,
        "email":email,
        "subject":subject,
        "message":message
    }
    return render(request,'pages/results.html', context)