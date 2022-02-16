from enum import unique
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator,PageNotAnInteger , EmptyPage
from django.utils.text import slugify

# Create your models here.

# Modelo para Goleador
@register_snippet
class Goleador(models.Model):
    rank = models.PositiveIntegerField(blank=True)
    nombre = models.CharField(max_length=255,blank=True)
    icono = models.URLField(max_length=255,blank=True)
    seleccion = models.CharField(max_length=255,blank=True)
    partidos = models.PositiveIntegerField(blank=True)
    goles = models.PositiveIntegerField(blank=True)
    penaltis = models.PositiveIntegerField(blank=True)
    media =  models.DecimalField(max_digits=3, decimal_places=2, blank=True)

    panels = [
        FieldPanel('rank'),
        FieldPanel('nombre'),
        FieldPanel('icono'),
        FieldPanel('seleccion'),
        FieldPanel('partidos'),
        FieldPanel('goles'),
        FieldPanel('penaltis'),
        FieldPanel('media'),
               
    ]

    def __str__(self):
        return f'{self.nombre}({self.goles})'

    class Meta:
        verbose_name_plural = 'goleadores'


# Page que mostrara el index de los goleadores
# Hereda de Home y no tendra descendientes
class GoleadoresIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):

        context = super().get_context(request)
        goleadores = Goleador.objects.all()

        context['goleadores'] = goleadores
    
        return context


