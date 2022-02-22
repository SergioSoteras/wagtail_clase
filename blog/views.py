from django.shortcuts import render
from django.views import generic
from blog.models import Noticia
# Create your views here.

#vista de un goleador
class NoticiaDetailView(generic.DetailView):
    model = Noticia
