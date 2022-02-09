from enum import unique
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator,PageNotAnInteger , EmptyPage
from django.utils.text import slugify

# Create your models here.

#Generos de las Peliculas
class Genre(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nombre
    panels = [
        FieldPanel('nombre')
    ]
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

# Modelo para Pelicula
@register_snippet
class Pelicula(models.Model):
    rating = models.DecimalField(max_digits=6, decimal_places=4, blank=True)
    slug = models.SlugField(max_length=255,blank=True)
    link = models.URLField(max_length=255,blank=True)
    place = models.PositiveIntegerField(blank=True)
    year = models.PositiveIntegerField("Año", blank=True)
    imagen = models.URLField(max_length=255,blank=True)
    title = models.CharField('título',max_length=255,blank=True)
    reparto = models.CharField(max_length=255,blank=True)
    generos = models.ManyToManyField(Genre)
    resumen = models.CharField(max_length=255,blank=True)
    duracion = models.CharField(max_length=255,blank=True)

    panels = [
        FieldPanel('rating'),
        FieldPanel('slug'),
        FieldPanel('link'),
        FieldPanel('place'),
        FieldPanel('year'),
        FieldPanel('imagen'),
        FieldPanel('title'),
        FieldPanel('reparto'),
        FieldPanel('generos'),
        FieldPanel('resumen'),
        FieldPanel('duracion'),       
    ]

    def generos_str(self):
        return ','.join([g.nombre for g in self.generos.all()])

    def __str__(self):
        return f'{self.title}({self.year})'

    class Meta:
        verbose_name_plural = 'peliculas'


# Page que mostrara el index de las peliculas
# Hereda de Home y no tendra descendientes
class PelisIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def paginate(self, request, peliculas, *args):
        page = request.GET.get('page')
        
        paginator = Paginator(peliculas, 15)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        decada = request.GET.get('decada')
        genero =  request.GET.get('genero')
        qs = ''
        if decada:
            peliculas = Pelicula.objects.filter(year__gte=1990, 
                year__lt=2000)
            qs = f'decada={decada}'

        elif genero:
            peliculas = Pelicula.objects.filter(generos__nombre__icontains = 'Drama')
            qs = f'genero={genero}'

        else:
            peliculas = Pelicula.objects.all()

        context['peliculas'] = Pelicula.objects.all() #self.paginate(request, peliculas)
        context['qs'] = qs
        
        return context



   