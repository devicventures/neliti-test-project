from django.shortcuts import render, redirect
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from .forms import DataForm
from .models import Cordinates
import json

# Create your views here.

def home(request):
    
    form = DataForm
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data.get('lat')
            lon = form.cleaned_data.get('lon')
            print(lat, lon)

            url = 'https://api.openweathermap.org/data/2.5/weather?'
            lattitude = 'lat='+str(lat)
            longitude = 'lon='+str(lon)
            key = '72a6382d9da49c3ce48c39855d690a56'


            url_link = url+lattitude+'&'+longitude+'&'+'appid='+key
            print(url)


            data = requests.get(url_link)
            data = data.json()
            print(data)
            
            temp = data.main.temp()


            print(temp)




        return redirect('weather')


    else:
        form = form
    
    context = {
        'form':form
    }

    return render(request, 'home.html', context)


class get_data(APIView):

    def get_form_data(request):

        # data= request.get('lat','lon')
        # print(data)

        data = requests.get(url_link)
        print(data)

        return JsonResponse(data)



def weather(request):

    form = DataForm
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data.get('lat')
            lon = form.cleaned_data.get('lon')
            print(lat, lon)

            #request.session[lat, lon] = request.POST['web_input']


        return redirect('weather')


    else:
        form = form

    context = {
        'form':form
    }

    return render(request, 'weather.html', context)