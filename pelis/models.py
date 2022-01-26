from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator

# Create your models here.

# Modelo para Pelicula
@register_snippet
class Pelicula(models.Model):
    rating = models.DecimalField(max_digits=6, decimal_places=4, blank=True)
    link = models.URLField(blank=True)
    place = models.PositiveIntegerField(blank=True)
    year = models.PositiveIntegerField("Año", blank=True)
    imagen = models.URLField(blank=True)
    title = models.CharField('título',max_length=255,blank=True)
    reparto = models.CharField(max_length=255,blank=True)
    genero = models.CharField(max_length=255,blank=True)
    resumen = models.CharField(max_length=255,blank=True)
    duracion = models.CharField(max_length=255,blank=True)

    panels = [
        FieldPanel('rating'),
        FieldPanel('link'),
        FieldPanel('place'),
        FieldPanel('year'),
        FieldPanel('imagen'),
        FieldPanel('title'),
        FieldPanel('reparto'),
        FieldPanel('genero'),
        FieldPanel('resumen'),
        FieldPanel('duracion'),
        
    ]

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

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        pelis_list = Pelicula.objects.all()
        paginator = Paginator(pelis_list, 20)
        context['peliculas'] = paginator.page(1)
        return context

   