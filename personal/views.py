from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location
import operator
from django.db.models import Q

from django.conf import settings
# Create your views here.
def home(request):
    '''
    This view handles request to the landing page, aka home page 
    '''

    query = request.GET.get('q', None)
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()

    if query is not None:
        images = images.filter(
           Q(category__name=query)|
           Q(location__name=query)
        )
    return render(request, 'home.html', {'images':images, 'categories':categories, 'locations':locations})
# 'media_url':settings.MEDIA_URL,
# def search(request, q):
#     query = request.GET.get('q', None)
#     qs = Category.objects.all()
#     if query is not None:
#         qs = qs.filter(name__icontains=query)
#     return render(request, 'search.html', {'qs':qs})

# if query is not None:
#         images = images.filter(
#             Q(name__icontains=query)|
#             Q(description__icontains=query)|
#             Q(location__icontains=query)
#         )