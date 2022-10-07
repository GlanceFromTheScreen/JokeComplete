from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from .models import User


def index(request):
    return HttpResponse("<h3>Hello</h3>")


def getinfo(request):
    print(Comments.objects.all())
    return HttpResponse("<h3>Hello</h3>")


data1 = 'data1'
data2 = 'data2'


def createUser(request):
    User.objects.create(username=data1, password=data2)
    return HttpResponse("<h3>User may be created</h3>")
