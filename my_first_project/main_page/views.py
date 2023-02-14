from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Dish

# Create your views here.
def main(request):
    categories = Category.objects.all() #.objects - uses to return data from BD in sequence

    return render(request, 'menu.html', context= {
        'categories': categories
    }) # specify ti which request respond to, next - tempale 




