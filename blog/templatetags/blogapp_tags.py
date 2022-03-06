from blog.models import BlogCategory as Category
from blog.models import BlogPage
from blog.models import FooterText as FooterText
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
    blogpages = BlogPage.objects.all()
    tags = []
    for blog in blogpages:
        for tag in blog.tags.all():
            tags.append(tag)
        
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

@register.inclusion_tag('components/footer_text.html',
                        takes_context=True)
def get_footer_text(context):
    footer_text = ""
    if FooterText.objects.first() is not None:
        footer_text = FooterText.objects.all()

    return {
        'footer_text': footer_text
    }