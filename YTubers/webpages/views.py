from django.shortcuts import render
from django.http import HttpResponse

from .models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    team = Team.objects.all()
    featured_youtuber = Youtuber.objects.order_by('-created_date').filter(is_featured = True)
    all_youtuber = Youtuber.objects.order_by('-created_date')
    
    data = {
        'slider' : sliders,
        'team':team,
        'featured_youtuber':featured_youtuber,
        'all_youtuber':all_youtuber
    }
    print(featured_youtuber)
    return render(request , "webpages/home.html",data)


def about(request):
    return render(request , "webpages/about.html")

def services(request):
    return render(request , "webpages/services.html")


def contract(request):
    return render(request , "webpages/contract.html")