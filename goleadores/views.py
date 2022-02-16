from django.shortcuts import render
from django.views import generic
from goleadores.models import Goleador
# Create your views here.

#vista de un goleador
class GoleadorDetailView(generic.DetailView):
    model = Goleador