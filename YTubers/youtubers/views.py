from django.shortcuts import render
from django.http import HttpResponse
from .models import Youtuber

# Create your views here.
def youtubers(request):
    ytubers = Youtuber.objects.order_by('-created_date')
    data={
        'ytubers' : ytubers
    }
    return render(request,'youtubers/tubers.html',data)

def youtubers_detail(request,id):
    ytuber = Youtuber.objects.filter(id=id).values()
    data={
        'ytuber' : ytuber[0]
    }

    return render(request,'youtubers/tubers_detail.html',data)

def search(request):
    ytubers = Youtuber.objects.order_by('-created_date')

    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()

    

    if 'key' in request.GET:
        keyword = request.GET['key']
        if keyword:
            ytubers = ytubers.filter(description__icontains = keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            ytubers = ytubers.filter(city__iexact = city)
            
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            ytubers = ytubers.filter(category__iexact = category)
            
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            ytubers = ytubers.filter(camera_type__iexact = camera_type)
            
    
    print(request.GET)

    data={
        'ytubers' : ytubers,
        'category_search':category_search,
        'camera_search':camera_search,
        'city_search':city_search
    }
    return render(request,'youtubers/search.html',data)

