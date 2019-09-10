from django.shortcuts import render, get_object_or_404
from page.models import FoodPage
# Create your views here.

def details(request, details):
    detailList = get_object_or_404(FoodPage, pk=details)
    data = FoodPage.objects.order_by('-info').filter(id=details)

    context = {
        'detailspage': data,
    }
    return render(request,'details//details.html', context)