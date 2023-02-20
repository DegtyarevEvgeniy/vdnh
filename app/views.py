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
    print("POST:", request.POST)
    if request.method == "POST":
        history = History.objects.create(
            points = request.POST.get('points[]'),
            time = request.POST.get('time'),
            distance = request.POST.get('distance'),
        )
        history.save()
    # print("BODY:", json.loads(request.body))
    # return JsonResponse({"status": "success"})
    # return JsonResponce()