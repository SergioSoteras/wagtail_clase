from blog.models import BlogCategory as Category
from blog.models import BlogPageTag as Tags
from blog.models import Noticia as Noticias
from django.template import Library, loader

register = Library()


@register.inclusion_tag('components/categories_list.html',
                        takes_context=True)
def categories_list(context):
    categories = Category.objects.all()
    return {
        'request': context['request'],
        'categories': categories
    }

@register.inclusion_tag('components/tags_list.html',
                        takes_context=True)
def tags_list(context):
    tags = Tags.objects.all()
    return {
        'request': context['request'],
        'tags': tags
    }

@register.inclusion_tag('components/noticias_list.html',
                        takes_context=True)
def noticias_list(context):
    noticias = Noticias.objects.all().order_by('-date')[:5]
    return {
        'request': context['request'],
        'noticias': noticias
    }