from django.shortcuts import render
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt

content = {}

def index_page(request):
    places = Place.objects.all()
    history = History.objects.all()
    content['places'] = [place for place in places]
    content['items'] = history


    return render(request, 'index.html', content)

@csrf_exempt


def save_page(request):
    if request.method == "POST":
        print("POST:", request.POST)
        f = dict(request.POST)

        s = ''
        for i in f:
            if 'coordinates' in i:
                s+=str(f[i])


        history = History.objects.create(
            points = f['points[]'],
            time = request.POST.get('time'),
            distance = request.POST.get('distance'),
            coordinates = s,
        )
        history.save()
    # print("BODY:", json.loads(request.body))
    # return JsonResponse({"status": "success"})
    # return JsonResponce()