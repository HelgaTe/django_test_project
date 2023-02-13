from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def events(request):
    return HttpResponse('<h1>Join and enjoy our upcoming events</h1>')
    
def list_events_year(request, year):
    return HttpResponse(f'<h1>Recall memories from {year}. It was awesome!</h1>')

def list_events_year_month(request, year, month):
    return HttpResponse(f'<h1>Memorable events in {month}-{year}. It was awesome!</h1>')