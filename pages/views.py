from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {
        'listings': listings,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'state_choices' : state_choices
    }
    return render(request, 'pages/index.html', context)
  

def about(request):
    realtors_mvp = Realtor.objects.all().filter(is_mvp=True)

    realtors = Realtor.objects.all()
    
    context = {
        'realtors_mvp': realtors_mvp,
        'realtors': realtors
    }
    return render(request, 'pages/about.html', context)  