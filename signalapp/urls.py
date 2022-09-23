from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import path, include
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Car

def home(request):
    return HttpResponse('Hello')

urlpatterns = [
    path('', home, name='home')
]

# from django.core.signals import request_finished
# from django.dispatch import receiver

# @receiver(request_finished)
# def my_callback1(sender, **kwargs):
#     print("Request finished!")
