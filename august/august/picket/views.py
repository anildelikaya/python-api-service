from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Accept a request, return a string
def home(request):
    return HttpResponse("API Service!, You're looking at Picket")

def signup(request):
    return HttpResponse(f"Account Registration: {datetime.now()}, You need a user name and passwoerd!")
   