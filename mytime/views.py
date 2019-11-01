from django.shortcuts import render
from django.http import  JsonResponse
from django.utils import timezone


# Create your views here.

def home(request):
    """
    Return server time to the client
    """
    return render(request,'mytime/home.htm',{'date':timezone.now()})

def get_time(request):
    """
    Return datetime data in json format
    """
    return JsonResponse({'date':timezone.now()})


