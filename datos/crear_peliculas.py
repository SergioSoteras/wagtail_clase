from pelis.models import Pelicula
import json

#for p in Pelicula.objects.all()
#   p.delete()

pelis = json.load(open('datos_pelis_plus.json'))

for p1 in pelis:
    p = Pelicula()
    p.title = p1['titulo']
    p.rating = p1['rating'].replace(",",".")
    p.link = 'https://www.imdb.com'+p1['url']
    p.place = p1['ranking']
    year = p1['year']
    if year.isdigit():
        p.year = p1['year']
    else:
        p.year= 0
    p.imagen = p1['img']
    p.reparto = p1['cast']
    p.genero = p1['genre']
    p.resumen = p1['description']
    p.duracion = p1['duracion']
    p.save()
