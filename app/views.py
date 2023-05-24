from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<marquee><h1>This is First FBV Page</h1></marquee>')
def second(request):
    return HttpResponse('<h1>This is the second FBV page<h1>')
def third(request):
    return render(request,'third.html')
def fourth(request):
    return render(request,'fourth.html')
