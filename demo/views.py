

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from requests import Response

from demo.models import Chicken


def homepage(request):
    chickens = Chicken.objects.all()
    return render(request, "exampleTemplate.html", {"chickens": list(chickens)})
