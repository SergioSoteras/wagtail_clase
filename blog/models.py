from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

class BlogIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['nombre'] = 'Sergio'
        return context

    subpage_types = ['BlogPage','ViajePage','PeliCommentPage',] #Añadir Viajes y Peli

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogPage(Page):
    date = models.DateField("Fecha Post")
    intro = models.CharField("Introduccion",max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Galleria de imágenes"),
    ]
    # NO PUEDE TENER HIJAS Y SOLO PUEDE SER HIJA DE BLOG INDEX PAGE
    parent_page_types = ['BlogIndexPage',]
    subpage_types = []

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

    # No puede tener paginas hijas
    subpage_types = []

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'

# NOTICIAS
@register_snippet
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    cuerpo = RichTextField(blank=True)
    date = models.DateField("Fecha Publicación")

    panels = [
        FieldPanel('titulo'),
        FieldPanel('cuerpo'),
        FieldPanel('date'),
    ]

    def __str__(self):
        return self.titulo

# PAGINA DE VIAJES
class ViajePage(Page):

    info = RichTextField(blank=True)
    coordenadas = models.CharField(max_length=250)
    
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('info', classname="full"),
            FieldPanel('coordenadas'),   
        ], heading="Imagenes del viaje"),
        InlinePanel('gallery_images', label="Galeria de imágenes"),
    ]
    # NO PUEDE TENER HIJAS Y SOLO PUEDE SER HIJA DE BLOG INDEX PAGE
    parent_page_types = ['BlogIndexPage',]
    subpage_types = []

class ViajePageGalleryImage(Orderable):
    page = ParentalKey(ViajePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

# PAGINA DE COMENTARIOS DE PELICULA
class PeliCommentPage(Page):

    comentario = RichTextField(blank=True)
    
    
    content_panels = Page.content_panels + [ 
        FieldPanel('comentario', classname="full"),  
        InlinePanel('peliculas', label='Peliculas'),]
    
    # NO PUEDE TENER HIJAS Y SOLO PUEDE SER HIJA DE BLOG INDEX PAGE
    parent_page_types = ['BlogIndexPage',]
    subpage_types = []

# orderable de peliculas para PeliCommentPage
class PeliCommentPeliculas(Orderable):
    page = ParentalKey(PeliCommentPage, on_delete=models.CASCADE, related_name='peliculas')
    pelicula = models.ForeignKey('pelis.Pelicula',null=True,blank=True,on_delete=models.SET_NULL,related_name='+')
    
    panels = [
        SnippetChooserPanel('pelicula')
    ]