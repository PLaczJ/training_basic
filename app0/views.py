

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from requests import Response


from demo.models import {{Model}}


def homepage(request):
    objs = {{Model}}.objects.all()
    return render(request, "exampleTemplate.html", {"model": list(objs)})
