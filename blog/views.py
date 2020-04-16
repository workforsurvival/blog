from django.shortcuts import render
from .models import Item

# Create your views here.


def home_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home-page.html', context)


def contact_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'contact.html', context)


def category_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'category-page.html', context)


def post_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'post-page.html', context)
