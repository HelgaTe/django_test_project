from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    return HttpResponse('<h1>Welcome on CAFE MAIN page</h1>')

def main_menu(request):
    return HttpResponse('<h1>Check the MENU page and treat yourself to delicious coffee</h1>')