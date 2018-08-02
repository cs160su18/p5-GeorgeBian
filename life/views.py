from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    all_kids = Kid.objects.all()
    return render(request, 'life/index.html', {"kids": all_kids})