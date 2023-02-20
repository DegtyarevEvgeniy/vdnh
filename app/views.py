from django.shortcuts import render
from .models import *

content = {}

def index_page(request):
    places = Place.objects.all()
    content['places'] = [place for place in places]

    return render(request, 'index.html', content)


def save_page(request):
    if request.method == 'POST':
        print(request.POST)
        return 
    # return JsonResponce()