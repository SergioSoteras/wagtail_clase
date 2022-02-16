from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from pelis.models import Pelicula,Genre

'''
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:
INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)
or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html
This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
'''


class GenerosAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = Genre
    menu_label = 'Géneros'
    search_fields = ('nombre',)
    menu_icon = 'group'

class PelisAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = Pelicula
    search_fields = ('title', 'reparto', 'year')
    list_display = ('title', 'reparto','year')
    list_filter = ('year',)
    menu_icon = 'media' 
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)



class PelisAdminGroup(ModelAdminGroup):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    menu_label = 'Películas'
    menu_icon = 'media' 
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (GenerosAdmin, PelisAdmin, )


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(PelisAdminGroup)