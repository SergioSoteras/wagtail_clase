from django.shortcuts import render
from django.views import generic
from blog.models import NoticiaBlog
# Create your views here.

#vista de un goleador
class NoticiaBlogDetailView(generic.DetailView):
    model = NoticiaBlog
