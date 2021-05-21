from django.shortcuts import render,redirect,reverse,HttpResponse
import json
import requests
from django.http import JsonResponse
from django.views import View

# Create your views here.

def getData():
    url = 'http://localhost:6800/schedule.json'
    data = {'project': 'four', 'spider': 'itcast'}
    print(requests.post(url=url, data=data))

def index(request):
    if request.method == 'POST':
        getData()
        return JsonResponse({'result':'OK'})
    return render(request,'index.html')

        