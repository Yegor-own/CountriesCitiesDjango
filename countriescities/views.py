from django.shortcuts import render
from django.http import HttpResponse
from .models import Countries, Cities

# Create your views here.

def index(request):
    countries = Countries.objects.order_by("id")
    out = ", ".join([c.name for c in countries])
    return HttpResponse(out)

def country(request, country_id):
    # country = Countries.objects.first()
    return HttpResponse("Country %s" % country_id)

def city(request, country_id, city_id):
    return HttpResponse("City %s" % city_id)