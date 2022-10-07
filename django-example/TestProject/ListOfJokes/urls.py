from django.urls import path
from django.conf.urls import url

from django.views.generic import ListView, DetailView
from . import views
from ListOfJokes.models import StartPhrases

urlpatterns = [
    path('', views.createUser, name='index'),
    url(r'^joke-list$', ListView.as_view(queryset=StartPhrases.objects.all().order_by("id")[:10],
                                        template_name="jokes/jokes.html")),
    url(r'joke-list/(?P<pk>\d+)$', DetailView.as_view(model=StartPhrases, template_name="jokes/one_joke.html"))
]