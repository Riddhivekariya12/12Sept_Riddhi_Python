from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url="https://data.covid19india.org/data.json"

    req=requests.get(url)
    data=req.json()
    print(data)
    return render(request,'index.html',{'data':data})


