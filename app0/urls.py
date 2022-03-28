from django.urls import path

from demo.views import homepage

urlpatterns = [path("", homepage)]