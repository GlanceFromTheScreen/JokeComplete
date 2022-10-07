from django.shortcuts import render


def index(request):
    return render(request, 'MainPage/HomePage.html')


Dict = {'values': ['data1', 'data2']}


def connect(request):
    return render(request, 'MainPage/basic.html', Dict)
